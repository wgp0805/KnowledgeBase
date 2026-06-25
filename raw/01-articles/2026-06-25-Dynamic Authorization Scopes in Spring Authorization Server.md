---
title: "Dynamic Authorization Scopes in Spring Authorization Server"
source: "Baeldung"
url: "https://feeds.feedblitz.com/~/958357049/0/baeldung"
date: "Wed, 24 Jun 2026 10:09:15 +0000"
score: 1.0
tags: ["Java", "Spring", "教程", "实践"]
auto_captured: true
---

# Dynamic Authorization Scopes in Spring Authorization Server

> **来源**: Baeldung  
> **链接**: https://feeds.feedblitz.com/~/958357049/0/baeldung  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 1.0

![](https://www.baeldung.com/wp-content/uploads/2024/11/Spring-Featured-Image-11-1024x536.jpg)

## 1\. Introduction

In this tutorial, we’ll show how to extend the Spring Authorization Server to handle dynamic OAuth 2.0 scopes, which are required in advanced authentication/authorization use cases.

## 2\. When to Use Dynamic Scopes?

OAuth2-based applications use scopes to request access tokens with a defined set of privileges, like reading fields from a user’s profile, performing an automation task, and so on. Usually, the scopes are fixed and known in advance both by the authorization server and the client application. In some scenarios, however, this is not the case.

**For instance, suppose your client application needs an access token to execute a single operation, like a transfer request or updating sensitive information**. One option is to implement a custom authorization scheme between the client and the resource server, but we’d be reinventing the wheel. From a security perspective, this is also not ideal, since it implies a bigger surface attack, as those protocols would need to be implemented across every resource server and client.

This is where dynamic scopes come into play. **In a nutshell, a dynamic scope is one that a client can request, but it ’s not known beforehand by the authorization server.**

Usually, a dynamic scope requires some sort of validation service to exist, so it can be validated. In practical terms, this requires a consent repository to store the requested scope, which will be used to validate it and, if the end user grants it, to update its status.

**When the client receives the access token, it will have the dynamic scope associated with it, allowing it to complete the desired operation.**

## 3\. Dynamic Scopes in Spring Authorization Server

The Spring Authorization Server, true to its roots, has a modular architecture, **which allows us to replace many of its components with custom ones**. We’ve already explored this characteristic [to implement multitenancy support](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/spring-multitenancy>), a feature not available by default. In our case, these are the aspects we need to modify:

  * Scope validation logic
  * Consent Validation
  * Consent page: optional, but usually required



Moreover, it’s a good idea to separate the Spring-specific code from the actual scope validation logic. We’ll create a _DynamicScopeService_ for that purpose, leaving to a _@Configuration_ class the task of creating an adapter between the expected method’s signature and the service.

Now, let’s move to the implementation.

## 4\. Project Setup

Dynamic Scopes don’t need any extra dependencies besides those needed by the Spring Authorization Server itself:
    
    
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security-oauth2-authorization-server</artifactId>
        <version>4.1.0</version>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security-oauth2-authorization-server-test</artifactId>
        <version>4.1.0</version>
        <scope>test</scope>
    </dependency>
    

The latest versions of these dependencies are available on Maven Central:

  * _[spring-boot-starter-security-oauth2-authorization-server](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-security-oauth2-authorization-server>)_
  * _[spring-boot-starter-security-oauth2-authorization-server-test](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-security-oauth2-authorization-server-test>)_



## 5\. Security Configuration

The Spring Authorization Server needs two security filter chains to operate:

  * one for handling OAuth/OIDC protocol endpoints
  * a “catch-all” chain that handles everything else, including user authentication



As usual in Spring Security, the built-in ones are only created when there are no application-defined chains available. **In our case, we need to tweak just the first one, but by doing so, the auto-configuration for the catch-all chain will be disabled, so we ’ll need to provide both.**

### 5.1. Authorization Server Chain

This is the modified chain where we’ll add our customization logic:
    
    
    @Bean
    @Order(Ordered.HIGHEST_PRECEDENCE)
    SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http) {
        http.oauth2AuthorizationServer(authorizationServer -> {
            http.securityMatcher(authorizationServer.getEndpointsMatcher());
            authorizationServer
              .oidc(withDefaults())
              .authorizationEndpoint(ap -> {
                  ap.consentPage("/consent");
                  ap.authenticationProviders(providers -> {
                      providers.stream()
                        .filter(OAuth2AuthorizationCodeRequestAuthenticationProvider.class::isInstance)
                        .map(p -> (OAuth2AuthorizationCodeRequestAuthenticationProvider)p)
                        .findFirst()
                        .ifPresent(p -> {
                            p.setAuthenticationValidator(dynamicScopesAuthenticationValidator());
                            p.setAuthorizationConsentRequired(dynamicScopesConsentValidator());
                        });
                  });
              });
        });
        http.authorizeHttpRequests(authorize -> authorize.anyRequest().authenticated());
        http.oauth2ResourceServer(resourceServer -> resourceServer.jwt(withDefaults()));
        http.exceptionHandling(exceptions -> exceptions.defaultAuthenticationEntryPointFor(
          new LoginUrlAuthenticationEntryPoint("/login"), createRequestMatcher()));
        return http.build();
    }
    

The scope validation takes place at the _OAuth2AuthorizationCodeRequestAuthenticationProvider_ , which uses two collaborating objects to perform its task:

  * An _AuthenticationValidator_ to validate the submitted parameters
  * A _Predicate_ that decides whether to ask for consent



Since the authorization server uses multiple _AuthenticationProvider_ s in its implementation, we need to go through all of them until we find the proper one. All this happens in the _authorizationEndpointCustomizer_ , which exposes the list of authentication providers.

The same customizer also allows us to set the _URI_ for a custom consent page, which will be “/consent” in our case. We’ll come back to the consent page later in this tutorial.

### 5.2. “Catch-All” Chain

This chain, which has no _securityMatcher()_ call in its DSL, will apply the following rules to incoming requests:

  * Any request must be authenticated
  * When receiving a non-authenticated request, use form-based login with default settings


    
    
    @Bean
    @Order(SecurityFilterProperties.BASIC_AUTH_ORDER)
    SecurityFilterChain defaultSecurityFilterChain(HttpSecurity http) {
        http.authorizeHttpRequests(authorize -> {
            authorize.anyRequest().authenticated();
          })
          .formLogin(withDefaults());
        return http.build();
    }
    

Here, we’re just replicating the default configuration. In a real-world scenario, we’d probably want to change some aspects of its properties. For instance, this is where we’d provide the _URI_ for a custom login page, enable two-factor authentication, or add support for a federated identity provider.

## 6\. Scope Validation

The _dynamicScopesAuthenticationValidator()_ method creates an adapter that isolates the Spring Security aspects of the scope validation from the business logic.

In our tutorial, we’ll assume that the dynamic scope will be a string that starts with the “TX:” prefix, followed by a unique transaction identifier. When a client needs an access token with this scope, it must add it to the scope request parameter of an authentication request, as in this example:
    
    
    https://idp/oauth2/authorize?scope=openid TX:1234&...other params omitted

The authentication provider will perform the standard validation steps and, eventually, will call our adapter to perform the validation logic:
    
    
    private Consumer<OAuth2AuthorizationCodeRequestAuthenticationContext> dynamicScopesAuthenticationValidator() {
        return ctx -> {
            OAuth2AuthorizationCodeRequestAuthenticationToken auth = ctx.getAuthentication();
            var requestedScopes = new HashSet<>(auth.getScopes());
            if ( requestedScopes.isEmpty() ) {
                return;
            }
            var registeredClient = ctx.getRegisteredClient();
            var allowedScopes = registeredClient.getScopes();
            requestedScopes.removeIf(allowedScopes::contains);
            if (requestedScopes.isEmpty() ) {
                return;
            }
            // Now, let's validate the remaining scopes using the provided validation service
            try {
                if (!dynamicScopeService.validate(registeredClient.getId(), requestedScopes)) {
                    throw new OAuth2AuthorizationCodeRequestAuthenticationException(
                      new OAuth2Error(OAuth2ErrorCodes.INVALID_SCOPE),
                      auth
                    );
                }
            } catch (Exception ex) {
                throw new OAuth2AuthorizationCodeRequestAuthenticationException(
                  new OAuth2Error(OAuth2ErrorCodes.SERVER_ERROR), 
                  ex, 
                  auth
                );
            }
        };
    }
    

The adapter receives an _OAuth2AuthorizationCodeRequestAuthenticationContext_ instance that contains information about the authorization request. **Notice that, at this point, the end user is not yet known, so we can ’t use it as part of this logic**.

These are the steps performed by the adapter:

  * Firstly, recover the requested scopes and client information from the context.
  * Secondly, remove any static scopes from the list.
  * If there are no dynamic scopes, return immediately
  * Otherwise, pass the client identifier and dynamic scopes to the validation service



The validation service’s job is to return just a yes/no answer depending on whether the request should be authorized. Our implementation, [available online](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://github.com/eugenp/tutorials/tree/master/spring-security-modules/spring-security-auth-server/src/main/java/com/baeldung/auth/server/dynamicscopes/components/impl/DynamicScopeServiceImpl.java>), just checks for a valid pattern. A real-world one would perform more complex validation, such as querying a database and applying any rules required by the specific use case.

## 7\. Consent Validation

The other tweak we’ve made to support dynamic scopes is to add custom logic to determine whether the authorization needs to ask for user consent before issuing an access token. **This was done using the AuthenticationProvider ’s _setAuthorizationConsentRequentid()_ method, which accepts a _Predicate_ argument.**

This _Predicate_ should return _true_ when an authorization request needs user consent, and  _false_ otherwise. As we’ve done in the scope validation case, we’ll use an adapter to extract the client’s identifier and requested scopes from the _OAuth2AuthorizationCodeRequestAuthenticationContext_ instance passed to the _Predicate_. Once the basic checks are done, we invoke the validation service to get a final decision about the consent:
    
    
    private Predicate<OAuth2AuthorizationCodeRequestAuthenticationContext> dynamicScopesConsentValidator() {
        return ctx -> {
            var previousConsent = ctx.getAuthorizationConsent();
            if ( previousConsent == null ) {
                // First consent, so consent is required
                return true;
            }
            OAuth2AuthorizationCodeRequestAuthenticationToken auth = ctx.getAuthentication();
            var requestedScopes = new HashSet<>(auth.getScopes());
            if ( requestedScopes.isEmpty() ) {
                return false;
            }
            // Remove already consented scopes
            var alreadyConsented = new HashSet<>(previousConsent .getScopes());		
            requestedScopes.removeIf(alreadyConsented::contains);
            if (requestedScopes.isEmpty() ) {
                return false;
            }
            // Any remaining scopes are dynamic scopes or static ones with no previous consent
            return dynamicScopeService.isConsentNeeded(ctx.getRegisteredClient().getId(), requestedScopes);
        };
    }
    

A key distinction of this validation is that it happens after a successful authentication. **This means that the business logic can use any of the standard Spring Security methods to get information about the current user and use it as part of the decision logic**.

## 8\. Consent Page

This page will be displayed to the user after a successful authentication, right before issuing an authorization code to a client application.

**From the user agent ’s perspective, this page will be accessed through a redirect from the login page**. The _Location_ header will point to the configured _URI_ along with the following query parameters:

  * _client_id_ : Client application’s identifier
  * _scope_ : Requested scopes
  * _state_ : Server-side state associated with the current authorization request.



**Please note that the state parameter in this case has no relation to the one with the same name that ’s included in the initial authorization _URL_ created by the client!**

Let’s implement a simple controller that takes these parameters, prepares a Model, and forwards the request to a view:
    
    
    @Controller
    public class ConsentController {
        private final RegisteredClientRepository registeredClientRepository;
        private final OAuth2AuthorizationConsentService authorizationConsentService;
        // ... constructor omitted
        @GetMapping("/consent")
        public String consent(Principal principal, Model model,
          @RequestParam(name = OAuth2ParameterNames.CLIENT_ID) String clientId,
          @RequestParam(name = OAuth2ParameterNames.SCOPE) String scope,
          @RequestParam(name = OAuth2ParameterNames.STATE) String state) {
            var client = registeredClientRepository.findByClientId(clientId);
            assert client != null;
            var currentConsent =  authorizationConsentService.findById(client.getId(), principal.getName());
            Set<String> authorizedScopes = currentConsent != null ? currentConsent.getScopes() : Set.of();
            // Remove already authorized scopes from the requested scopes and the special 'openid' scope.
            var neededScopes = Set.of(scope.split(" ")).stream()
              .filter(s -> !authorizedScopes.contains(s) && !OidcScopes.OPENID.equals(s))
              .toList();
            model.addAttribute("clientId", clientId);
            model.addAttribute(
              "clientName", 
              client.getClientName() != null ? client.getClientName() : client.getClientId()
            );
            model.addAttribute("scopes", neededScopes);
            model.addAttribute("state", state);
            model.addAttribute("authorizedScopes", authorizedScopes);
            return "consent";
       }
    }
    

We’ve injected two services in this controller to look for additional information needed to build the view:

  * _registeredClientRepository_ : Allow us to retrieve detailed information for the client, given its identifier
  * _authorizationConsentService_ : Returns an _OAuthAuthorizationConsent_ containing all consents given to a client by a user



We use those services to build a list of the newly required consents and store it in a Spring MVC _Model_.

Here, we could also query a business service to enrich the _Model_ with details related to any requested dynamic scope. For instance, if our dynamic scope represents a transfer request, we could look up its details and include them in the model.

[The view itself](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://github.com/eugenp/tutorials/tree/master/spring-security-modules/spring-security-auth-server/src/main/resources/templates/consent.html>) uses a Thymeleaf template to display the consent request and present to the user an option to accept or deny it.**Note that the form ’s submit target is, by default, protected with a CSRF token, so make sure to use the th:action=” _@{/path} ”_ syntax**. Thanks to [Thymeleaf’s Spring integration](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.thymeleaf.org/doc/tutorials/3.1/thymeleafspring.html#integration-with-requestdatavalueprocessor>), this will automatically include a hidden input field with the correct CSRF token value.

Last, but not least, note that the form’s action target should point to the server’s OAuth2 authorization endpoint. Later, if we decide to change this _URI_ from the default value, we must make sure that this form points to the same place.

## 9\. Testing

Now, let’s write a test to verify our customized authorization server’s behavior, at least for the “happy path” case. The [full code](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://github.com/eugenp/tutorials/tree/master/spring-security-modules/spring-security-auth-server/src/test/java/com/baeldung/auth/server/dynamicscopes/DynamicScopesAuthServerUnitTest.java>) is a bit long, so here we’ll just discuss the main caveats when implementing it.

The first thing is that, to validate end-to-end calls, it’s better to use an environment that’s close to the real one. This is why we use _WebEnvironment.RANDOM_PORT_ , **which starts a full servlet stack bound to a free local port.** The port’s actual value is injected into the test using the _@LocalPort_ annotation, so we can use it to build all request _URLs_.

Secondly, we need to be able to keep session cookies between requests sent throughout the authentication/authorization process. This means we need to configure a _RestTestClient_ with a factory request with this support enabled.

In our case, there’s another issue. We can instruct a _RestTestClient_ to either follow all redirects or none. However, once configured, it’s not trivial to modify this behavior. We could opt to use manual redirect handling only, but that would require additional coding. **Instead, we ’ve opted to define two clients: one that follows redirects, and another that doesn’t**. Both clients share the same _CookieManager_ instance, so we can use either one in the test without getting into session-related issues:
    
    
    @BeforeEach
    void setupRestClient() {
        CookieManager cookieManager = new CookieManager();
        var followRedirectsHttpClient = HttpClient.newBuilder()
          .followRedirects(HttpClient.Redirect.ALWAYS)
          .cookieHandler(cookieManager)
          .build();
        var followRedirectsRequestFactory = new JdkClientHttpRequestFactory(followRedirectsHttpClient);
        restTestClient = RestTestClient
          .bindToServer(followRedirectsRequestFactory)
          .baseUrl("http://localhost:" + port)
          .build();
        var noRedirectsHttpClient = HttpClient.newBuilder()
          .followRedirects(HttpClient.Redirect.NEVER)
          .cookieHandler(cookieManager)
          .build();
        var noRedirectsRequestFactory = new JdkClientHttpRequestFactory(noRedirectsHttpClient);
        noRedirecRestTestClient = RestTestClient
          .bindToServer(noRedirectsRequestFactory)
          .baseUrl("http://localhost:" + port)
          .build();
    }
    

Our “happy-path” test covers the following:

  * Endpoint discovery
  * Building an authorization request with a dynamic scope
  * Submitting user credentials to the login form
  * Submitting values in the consent form
  * Using the generated authentication code to retrieve an access token
  * Validate that the access token has the request dynamic scope associated with it



**Those steps cover a complete authorization flow, producing an access token that we can use to send a request to a resource server.**

## 10\. Conclusion

In this tutorial, we’ve seen how we can modify the Spring Authorization Server’s default configuration to support dynamic scopes. This expands the range of use cases where we can use it, making it a suitable candidate for complex authorization-related scenarios.

As always, the full source code is available [over on GitHub](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://github.com/eugenp/tutorials/tree/master/spring-security-modules/spring-security-auth-server>).

The post [Dynamic Authorization Scopes in Spring Authorization Server](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/java-spring-dynamic-authorization-scopes>) first appeared on [Baeldung](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com>).![](assets/2026-06-25-Dynamic%20Authorization%20Scopes%20in%20Spring%20Authorization%20Server/c61523524869b85ae6e42eabadb5a262_MD5.gif)

[![](assets/2026-06-25-Dynamic%20Authorization%20Scopes%20in%20Spring%20Authorization%20Server/93bb369a69d36dd82e002d18ff7cf602_MD5.png)](<https://feeds.feedblitz.com/_/28/958357049/baeldung>) [![](assets/2026-06-25-Dynamic%20Authorization%20Scopes%20in%20Spring%20Authorization%20Server/6af7991c4c6f5641c538d61a5608fb0b_MD5.png)](<https://feeds.feedblitz.com/_/29/958357049/baeldung,https%3a%2f%2fwww.baeldung.com%2fwp-content%2fuploads%2f2024%2f11%2fSpring-Featured-Image-11-1024x536.jpg>) [![](assets/2026-06-25-Dynamic%20Authorization%20Scopes%20in%20Spring%20Authorization%20Server/533f73c805dddfc4d23114fef4ac7205_MD5.png)](<https://feeds.feedblitz.com/_/24/958357049/baeldung>) [![](assets/2026-06-25-Dynamic%20Authorization%20Scopes%20in%20Spring%20Authorization%20Server/0130cc048dca99e29c926804679b6308_MD5.png)](<https://feeds.feedblitz.com/_/19/958357049/baeldung>) [![](assets/2026-06-25-Dynamic%20Authorization%20Scopes%20in%20Spring%20Authorization%20Server/a12966c8b8df527e61bbaa696ddbdf28_MD5.png)](<https://feeds.feedblitz.com/_/20/958357049/baeldung>) [![](assets/2026-06-25-Dynamic%20Authorization%20Scopes%20in%20Spring%20Authorization%20Server/a0674e7cd29f2bb749a6b32c7acdbbda_MD5.png)](<https://www.baeldung.com/java-spring-dynamic-authorization-scopes#respond> "View Comments") [![](assets/2026-06-25-Dynamic%20Authorization%20Scopes%20in%20Spring%20Authorization%20Server/074e9c5c0cc83cd9f21c55921090b857_MD5.png)](<https://www.baeldung.com/java-spring-dynamic-authorization-scopes/feed> "Follow Comments via RSS")


---
> 原文链接: https://feeds.feedblitz.com/~/958357049/0/baeldung