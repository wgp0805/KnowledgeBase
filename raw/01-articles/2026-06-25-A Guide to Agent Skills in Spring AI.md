---
title: "A Guide to Agent Skills in Spring AI"
source: "Baeldung"
url: "https://feeds.feedblitz.com/~/958380014/0/baeldung"
date: "Wed, 24 Jun 2026 10:26:06 +0000"
score: 1.0
tags: ["Java", "Spring", "教程", "实践"]
auto_captured: true
---

# A Guide to Agent Skills in Spring AI

> **来源**: Baeldung  
> **链接**: https://feeds.feedblitz.com/~/958380014/0/baeldung  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 1.0

![](https://www.baeldung.com/wp-content/uploads/2024/11/Spring-Featured-Image-10-1024x536.jpg)

## 1\. Overview

Modern web applications are increasingly integrating with [Large Language Models (LLMs)](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/cs/large-language-models>) to build solutions that go beyond simple question answering. To create AI agents capable of handling complex user requests, we often connect them to multiple [Model Context Protocol (MCP)](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/spring-ai-model-context-protocol-mcp>) servers that provide them with specific capabilities via tools.

However, creating and running MCP servers can be overkill for lightweight and local automation tasks where we just need to expose a simple capability to a single agent.

[Agent Skills](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://agentskills.io/home>) is a specification that provides a structured way to locally define, package, and expose these capabilities to an AI agent.

In this tutorial, we’ll explore the Agent Skills capability in Spring AI. We’ll configure a custom skill and integrate it with a simple chatbot to summarize articles.

## 2\. What are Agent Skills?

**Agent Skills is an open specification for defining various capabilities that an AI agent can invoke**. **A skill is essentially a directory containing a _SKILL.md_ file, which acts as its manifest, alongside any associated code** like Python or Bash scripts, or additional resources that the skill relies on.

The _SKILL.md_ file contains a frontmatter block with a name and description, followed by a set of natural language instructions that tell the agent how to use the skill.

**When the agent receives a user request, it reads the descriptions of all available skills and decides if any is relevant**. If yes, it then loads the relevant files into context and follows the instructions inside the matching skill to fulfill the request. And if no skill matches the request, the agent simply responds using its general capabilities without invoking any skill.

We’ll see an agent invoking our custom skill practically in action in the upcoming sections.

## 3\. Setting up the Project

Before we dive into the implementation, we’ll need to include the necessary dependencies and configure our application correctly.

### 3.1. Dependencies

Let’s start by adding the necessary dependencies to our project’s _pom.xml_ file:
    
    
    <dependency>
        <groupId>org.springframework.ai</groupId>
        <artifactId>spring-ai-starter-model-openai</artifactId>
        <version>2.0.0</version>
    </dependency>
    <dependency>
        <groupId>org.springaicommunity</groupId>
        <artifactId>spring-ai-agent-utils</artifactId>
        <version>0.10.0</version>
    </dependency>

Here, we first import [Spring AI’s OpenAI starter dependency](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://mvnrepository.com/artifact/org.springframework.ai/spring-ai-starter-model-openai>), which we’ll use to interact with a chat model. Support for agent skills is available in Spring AI 2 and later, so we need to make sure we’re using the correct version.

Next, we import the [agent-utils dependency](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://mvnrepository.com/artifact/org.springaicommunity/spring-ai-agent-utils>) from the [Spring AI community](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~github.com/spring-ai-community>), which enables us to add the agent skills capability to our chat models.

### 3.2. Configuring a Chat Model

Next, let’s configure our [OpenAI API key](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://platform.openai.com/api-keys>) and [chat model](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://developers.openai.com/api/docs/models>) in the _application.yaml_ file:
    
    
    spring:
      ai:
        openai:
          api-key: ${OPENAI_API_KEY}
          chat:
            options:
              model: gpt-5.5

We use the _${}_ property placeholder to load the value of our API Key from an [environment variable](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/spring-boot-properties-env-variables#use-environment-variable-in-applicationyml-file>).

Additionally, we specify OpenAI’s [GPT 5.5](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://openai.com/index/introducing-gpt-5-5/>) model using the _gpt-5.5_ model ID. Alternatively, we can use a different chat model that supports the agent skills specification, as the specific AI model or provider is irrelevant for this demonstration.

With these two properties set, **Spring AI automatically creates a bean of type _ChatModel_ , allowing us to interact with the specified model**.

## 4\. Defining Our Custom Skill

Now let’s define a custom agent skill that can fetch an article from a URL and summarize it.

Agent skills follow a specific directory structure, so let’s set that up. **We ’ll start by creating an _.openai/skills_ directory in our project’s root directory. We can define multiple subdirectories inside this, each representing a distinct agent skill**.

Next, **we ’ll create an _article-summarizer_ subdirectory to represent our custom skill inside .openai/skills** and define our main _SKILL.md_ file inside it:
    
    
    ---
    name: article-summarizer
    description: Summarizes articles into concise digests. Useful when user asks to summarize or get key points from an article.
    ---
    # Article Summarizer
    ## Instructions
    When summarizing an article:
    1. If given a URL: Run `uv run scripts/fetch_article.py <url>` to retrieve the content.
    2. Once content is available, extract the main thesis, few key points, and conclusion.
    3. Structure the output as a TL;DR, key points, and a bottom line.

In the [frontmatter block](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter>), we define the name and description of our skill. **The description is especially important as the agent uses it to determine whether this skill is relevant for a given user request**. Next, we define the instructions that tells the agent exactly what steps to follow when the skill is invoked, including which script to run and how to structure the final output.

Next, let’s create the _fetch_article.py_ script inside a new _scripts_ subdirectory that we reference in the instructions:
    
    
    ARTICLE = """
    ... hardcoding sample article for demonstration
    """
    print(ARTICLE)

Here, for our demonstration, we simply print a [hardcoded article about MCP elicitations](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/spring-ai-mcp-elicitations>) instead of actually making a web request. **The AI model will run this script and read the standard output to get this article ’s content regardless of the URL in the request **.

Also, **it ’s important to note that we can define our scripts in any language of our choice**. We just need to make sure that we pre-install the required runtimes for our agent to execute the necessary commands.

## 5\. Creating a Simple Chatbot

With our configurations in place, let’s build a simple chatbot.

In Spring AI, **the _ChatClient_ class acts as the main entry point for interacting with our configured chat completion model**. Let’s define its bean using the auto-configured _ChatModel_ bean:
    
    
    @Bean
    ChatClient chatClient(ChatModel chatModel) {
        String skillsRootDirectory = ".openai/skills";
        return ChatClient
          .builder(chatModel)
          .defaultTools(
            SkillsTool.builder()
              .addSkillsDirectory(skillsRootDirectory)
              .build(),
            FileSystemTools.builder()
              .allowedDirectory(skillsRootDirectory)
              .build(),
            ShellTools.builder()
              .build()
          ).build();
    }

In our bean definition, **we first register our custom skills directory using _SkillsTool_ , pointing it to the _.openai/skills_ directory**.

Secondly, **we register _FileSystemTools_ , which gives the agent the ability to read and write any files on the local filesystem**. To restrict the tool’s operations to the configured skills directory, we use the _allowedDirectory()_ method.

Finally, **we register _ShellTools_ , which allows the agent to execute shell commands**, enabling it to run the Python script we’ve defined.

However, it’s important to note that _ShellTools_ executes our scripts directly on the local machine without [sandboxing](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/cs/sandboxing-fundamentals>). As such, **we should carefully review the scripts we expose to our agent** and consider [containerizing our application](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/dockerizing-spring-boot-application>) to limit potential exposure.

Next, let’s inject the _ChatClient_ bean in a controller class and expose a REST API:
    
    
    @PostMapping("/chat")
    ResponseEntity<ChatbotResponse> chat(@RequestBody ChatbotRequest chatbotRequest) {
        String answer = chatClient
          .prompt()
          .user(chatbotRequest.question)
          .call()
          .content();
        return ResponseEntity.ok(new ChatbotResponse(answer));
    }
    record ChatbotRequest(String question) {}
    record ChatbotResponse(String answer) {}

Here, we simply pass the user’s _question_ to the _chatClient_ instance and return the LLM’s response. We’ll use this API endpoint to interact with our chatbot in the upcoming section.

## 6\. Interacting With Our Chatbot

Now that we’ve built our implementation, let’s interact with our chatbot and test the agent skill capability.

We’ll use the [HTTPie](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/httpie-http-client-command-line>) CLI to invoke the chatbot’s API endpoint:
    
    
    http POST :8080/chat question="Can you summarize the following article: https://www.baeldung.com/sample-non-existing-article"

Here, we ask the chatbot to summarize a specific article by passing a URL in the question. **We deliberately provide the URL of a non-existent article to verify that the chatbot summarizes the article we ’ve hardcoded in our Python script**.

Let’s see what we get as a response:
    
    
    {
      "answer": "## TL;DR\nThis article explains how to implement MCP Elicitations in Spring AI, allowing MCP servers to request additional user information dynamically during tool execution.
        \n\n## Key Points\n- MCP Elicitations solve the problem of missing user information during MCP tool execution.
        \n- The tutorial demonstrates building an MCP server using Spring AI.
        \n- The MCP server exposes a tool that fetches author details and conditionally requests additional information.
        \n- The `elicit()` method is used to pause execution and gather required details from the user.
        \n- The article also demonstrates configuring an MCP client and integrating it with an Anthropic Claude model
        \n- Spring AI automatically creates MCP clients and tool callback providers from configuration.
        \n- An `@McpElicitation` handler is used on the client side to respond to elicitation requests.
        \n- The tutorial concludes with a working chatbot example and log outputs showing the complete elicitation flow.
        \n\n## Bottom Line\nMCP Elicitations enable interactive AI applications where tools can dynamically collect additional context from users during execution,
        making MCP-based systems more flexible and user-aware."
    }

As we can see, **the LLM summarizes our hardcoded article and the response is structured exactly as our skill ’s instructions prescribed, with a TL;DR, a set of key points, and a bottom line**.

Behind the scenes, the agent matched the user’s request to the _article-summarizer_ skill based on its description, loaded the instructions into context using _FileSystemTools_ , executed the _fetch_article.py_ script via _ShellTools_ to retrieve the article content, and then structured the response following the instructions in our _SKILL.md_ file.

## 7\. Conclusion

In this article, we’ve explored the concept of Agent Skills using Spring AI.

We started by understanding what Agent Skills are and how they help us in exposing reusable capabilities to an AI agent.

Then, we defined a custom article summarizer skill and wired it into a chatbot. Finally, we interacted with our chatbot to confirm that it correctly discovers and invokes our skill.

As always, all the code examples used in this article are available [over on GitHub](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://github.com/eugenp/tutorials/tree/master/spring-ai-modules/spring-ai-agent-skills>).

The post [A Guide to Agent Skills in Spring AI](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/spring-ai-agent-skills>) first appeared on [Baeldung](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com>).![](assets/2026-06-25-A%20Guide%20to%20Agent%20Skills%20in%20Spring%20AI/c61523524869b85ae6e42eabadb5a262_MD5.gif)

[![](assets/2026-06-25-A%20Guide%20to%20Agent%20Skills%20in%20Spring%20AI/93bb369a69d36dd82e002d18ff7cf602_MD5.png)](<https://feeds.feedblitz.com/_/28/958380014/baeldung>) [![](assets/2026-06-25-A%20Guide%20to%20Agent%20Skills%20in%20Spring%20AI/6af7991c4c6f5641c538d61a5608fb0b_MD5.png)](<https://feeds.feedblitz.com/_/29/958380014/baeldung,https%3a%2f%2fwww.baeldung.com%2fwp-content%2fuploads%2f2024%2f11%2fSpring-Featured-Image-10-1024x536.jpg>) [![](assets/2026-06-25-A%20Guide%20to%20Agent%20Skills%20in%20Spring%20AI/533f73c805dddfc4d23114fef4ac7205_MD5.png)](<https://feeds.feedblitz.com/_/24/958380014/baeldung>) [![](assets/2026-06-25-A%20Guide%20to%20Agent%20Skills%20in%20Spring%20AI/0130cc048dca99e29c926804679b6308_MD5.png)](<https://feeds.feedblitz.com/_/19/958380014/baeldung>) [![](assets/2026-06-25-A%20Guide%20to%20Agent%20Skills%20in%20Spring%20AI/a12966c8b8df527e61bbaa696ddbdf28_MD5.png)](<https://feeds.feedblitz.com/_/20/958380014/baeldung>) [![](assets/2026-06-25-A%20Guide%20to%20Agent%20Skills%20in%20Spring%20AI/a0674e7cd29f2bb749a6b32c7acdbbda_MD5.png)](<https://www.baeldung.com/spring-ai-agent-skills#respond> "View Comments") [![](assets/2026-06-25-A%20Guide%20to%20Agent%20Skills%20in%20Spring%20AI/074e9c5c0cc83cd9f21c55921090b857_MD5.png)](<https://www.baeldung.com/spring-ai-agent-skills/feed> "Follow Comments via RSS")


---
> 原文链接: https://feeds.feedblitz.com/~/958380014/0/baeldung