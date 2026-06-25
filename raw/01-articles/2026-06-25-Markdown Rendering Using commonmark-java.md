---
title: "Markdown Rendering Using commonmark-java"
source: "Baeldung"
url: "https://feeds.feedblitz.com/~/958199054/0/baeldung"
date: "Fri, 19 Jun 2026 14:47:26 +0000"
score: 0.75
tags: ["Java", "Spring", "教程", "实践"]
auto_captured: true
---

# Markdown Rendering Using commonmark-java

> **来源**: Baeldung  
> **链接**: https://feeds.feedblitz.com/~/958199054/0/baeldung  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.75

![](https://www.baeldung.com/wp-content/uploads/2024/07/Java-Featured-10-1024x536.jpg)

## 1\. Overview

Manipulating Markdown content is a common programming task. [CommonMark](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://github.com/commonmark/commonmark-java>) is a Java library that simplifies working with Markdown documents.

In this tutorial, we’ll learn how to manipulate Markdown content using the library. We’ll see how to parse Markdown into HTML and convert HTML back into Markdown. Finally, we’ll explore how to customize nodes for advanced processing.

## 2\. _commonmark-java_ Library

The _commonmark-java_ library provides classes and interfaces for working with Markdown content based on the CommonMark specification. **It allows us to parse Markdown into HTML and convert HTML back into Markdown**. Additionally, it provides access to the Abstract Syntax Tree (AST), enabling further customization and processing.

To use the _common-java_ library, let’s add the [_commonmark_](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://mvnrepository.com/artifact/org.commonmark/commonmark>) dependency to our _pom.xml_ :
    
    
    <dependency>
        <groupId>org.commonmark</groupId>
        <artifactId>commonmark</artifactId>
        <version>0.28.0</version>
    </dependency>

The commark dependency provides classes such as _Parser_ , _HtmlRenderer_ , and _MarkdownRenderer_ for Markdown processing and rendering.

Additionally, CommonMark provides extension dependencies for more advanced processing features. Examples include [_commonmark-ext-gfm-tables_](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://mvnrepository.com/artifact/org.commonmark/commonmark-ext-gfm-tables>) for GitHub Flavored Markdown tables and [_commonmark-ext-gfm-alerts_](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://mvnrepository.com/artifact/org.commonmark/commonmark-ext-gfm-alerts>) for alert blocks.

## 3\. Parsing and Rendering Markdown to HTML

Moving on, let’s see one of the most common uses of the library: parsing Markdown and rendering it as HTML.

First, let’s define a method named _markDownToHtml()_ :
    
    
    public static String markDownToHtml(String markdown) {
        Parser parser = Parser.builder().build();
        Node document = parser.parse(markdown);
        HtmlRenderer renderer = HtmlRenderer.builder().build();
        return renderer.render(document);
    }

Here, we create an instance of _Parser_ to parse Markdown input into a document node. Next, **we create an _HtmlRenderer_ instance to render the parsed node as HTML**.

A _Node_ represents an element in the parsed Markdown document tree.

Then, let’s write a unit test to verify the result:
    
    
    @Test
    void givenMarkdownInput_whenConvertingToHtml_thenReturnRenderedHtml() {
        String html = markDownToHtml("Welcome to *Baeldung*");
        assertEquals("<p>Welcome to <em>Baeldung</em></p>\n", html);
    }

In the code above, we pass a string containing Markdown syntax to _markDownToHtml()_ method. Since _Baeldung_ is wrapped in asterisks (_*_), the Markdown parser interprets it as emphasized text. Consequently, the renderer converts it to an HTML _< em>_ element.

## 4\. Processing Parsed Nodes

Furthermore, we can use a [visitor](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/java-visitor-pattern>) to further process nodes in the parsed document tree. The library allows us to extend the _AbstractVisitor_ class to process a node.

Let’s create a visitor class that counts every word in a sentence:
    
    
    class WordCountVisitor extends AbstractVisitor {
        int wordCount = 0;
        @Override
        public void visit(Text text) {
            wordCount += text.getLiteral().split("\\w+").length;
            visitChildren(text);
        }
    }

Next, let’s write a method that uses the visitor:
    
    
    public static int processParsedNode(String markdown) {
        Parser parser = Parser.builder().build();
        Node node = parser.parse(markdown);
        WordCountVisitor visitor = new WordCountVisitor();
        node.accept(visitor);
        return visitor.wordCount;
    }

In the method above, we create a _WordCountVisitor_ object and pass it to the parsed node for processing.

Let’s write a unit test to confirm the method:
    
    
    @Test
    void givenMarkdownInput_whenProcessingParsedNode_thenReturnWordCount() {
        int wordCount = processParsedNode("Welcome to *Baeldung*");
        assertEquals(3, wordCount);
    }

Here, we verify that the expected word count is equal to the actual word count.

## 5\. Rendering HTML to Markdown

Furthermore, CommonMark also provides classes for rendering HTML-like document structures into Markdown format, making it a library for both HTML and Markdown processing.

Let’s see this in action by writing code that converts an HTML heading into a Markdown format:
    
    
    public static String htmlToMarkDown(String htmlHeading) {
        Heading heading = new Heading();
        heading.setLevel(2);
        heading.appendChild(new Text(htmlHeading));
        Document document = new Document();
        document.appendChild(heading);
        MarkdownRenderer renderer = MarkdownRenderer.builder()
          .build();
        return renderer.render(document);
    }

In the code above, we create a _Heading_ object and set the level to _2_ , which represents an H2 heading. Next, we append a _Text_ object containing the heading content. **Finally, we use the _MarkdownRenderer_ builder to render the document as Markdown**.

Next, let’s write a unit test to confirm the output:
    
    
    @Test
    void givenHeadingText_whenConvertingToMarkdown_thenReturnMarkdownHeading() {
        String markdown = htmlToMarkDown("Java Tutorial");
        assertEquals("## Java Tutorial\n", markdown);
    }

In the code above, we verify that the renderer correctly converts the document structure into a valid Markdown output.

## 6\. Customizing HTML Rendering

Furthermore, CommonMark allows us to customize rendered HTML attributes using the _AttributeProvider_ interface.

Let’s see this in action by implementing a class custom image attribute provider:
    
    
    public class ImageAttributeProvider implements AttributeProvider {
        @Override
        public void setAttributes(Node node, String tagName, Map<String, String> attributes) {
            if (node instanceof Image) {
                attributes.put("class", "border");
            }
        }
    }

In the code above, we create a class named _ImageAttributeProvider_ that implements the _AttributeProvider_ interface. Inside the _setAttributes()_ method, we check whether the current node is an instance of _Image_. If it is, we add a _class_ attribute with the value “ _border_ “.

Next, let’s write a method that applies the custom attribute provider during HTML rendering:
    
    
    public static String changingHtmlAttribute(String source) {
        Parser parser = Parser.builder()
          .build();
        Node node = parser.parse(source);
        HtmlRenderer renderer = HtmlRenderer.builder()
          .attributeProviderFactory(context -> new ImageAttributeProvider())
          .build();
        return renderer.render(node);
    }

In the code above, we customize the _HtmlRenderer_ with a custom attribute provider using the _attributeProviderFactory()_ method. Using [lambda expressions](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/java-8-lambda-expressions-tips>), we invoke our provider for each node, allowing us to customize the generated HTML attributes. Every rendered image element receives a _class= ”border”_ attribute.

Finally, let’s write a unit test to ascertain the customized output:
    
    
    @Test
    void givenImageMarkdown_whenRenderingHtml_thenAddCustomClassAttribute() {
        String html = changingHtmlAttribute("![text](/url.png)");
        assertEquals("<p><img src=\"/url.png\" alt=\"text\" class=\"border\" /></p>\n", html);
    }

In the test above, we verify that the custom attribute provider successfully adds the _border_ CSS class to rendered image elements.

## 7\. Customizing Render Node

Moreover, the library allows us to customize how specific nodes are rendered by implementing the _NodeRenderer_ interface.

Let’s create a custom renderer for _IndentedCodeBlock_ nodes:
    
    
    public class IndentedCodeBlockNodeRenderer implements NodeRenderer {
        private final HtmlWriter html;
        public IndentedCodeBlockNodeRenderer(HtmlNodeRendererContext context) {
            this.html = context.getWriter();
        }
        @Override
        public Set<Class<? extends Node>> getNodeTypes() {
            return Set.of(IndentedCodeBlock.class);
        }
        @Override
        public void render(Node node) {
            IndentedCodeBlock codeBlock = (IndentedCodeBlock) node;
            html.line();
            html.tag("pre");
            html.text(codeBlock.getLiteral());
            html.tag("/pre");
            html.line();
        }
    }

In the code above, we implement the _NodeRenderer_ interface and specify that the renderer handles _IndentedCodeBlock_ nodes through the _getNodeTypes()_ method.

Then, in the _render()_ method, we manually generate the HTML output for the code block using _HtmlWriter_.

Next, let’s register the custom renderer with _HtmlRenderer_ :
    
    
    public static String customizingHtmlRendering(String source) {
        Parser parser = Parser.builder()
          .build();
        Node node = parser.parse(source);
        HtmlRenderer renderer = HtmlRenderer.builder()
          .nodeRendererFactory(IndentedCodeBlockNodeRenderer::new)
          .build();
        return renderer.render(node);
    }

Here, we customize the renderer using the _nodeRendererFactory()_ method. We invoke the custom node using a [method reference](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/java-method-references>). This allows the renderer to delegate matching nodes to our custom implementation during HTML generation

Let’s write a unit test to verify the _customizingHtmlRendering()_ method:
    
    
    @Test
    void givenIndentedCodeBlock_whenRenderingHtml_thenUseCustomNodeRenderer() {
        String html = customizingHtmlRendering("Example:\n\n    code");
        assertEquals("<p>Example:</p>\n<pre>code\n</pre>\n", html);
    }

Here, we verify that indented code blocks are rendered using our custom renderer implementation.

## 8\. Conclusion

In this article, we learned how to use the CommonMark library to parse Markdown into HTML and convert HTML back into Markdown. Additionally, we saw how to customize HTML attributes and node rendering for more advanced processing scenarios.

As always, the source code for the sample code is available [over on GitHub](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://github.com/eugenp/tutorials/tree/master/libraries-formatting>).

The post [Markdown Rendering Using commonmark-java](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com/java-commonmark-render-markdown>) first appeared on [Baeldung](<https://feeds.feedblitz.com/~/t/0/0/baeldung/~https://www.baeldung.com>).![](assets/2026-06-25-Markdown%20Rendering%20Using%20commonmark-java/c61523524869b85ae6e42eabadb5a262_MD5.gif)

[![](assets/2026-06-25-Markdown%20Rendering%20Using%20commonmark-java/93bb369a69d36dd82e002d18ff7cf602_MD5.png)](<https://feeds.feedblitz.com/_/28/958199054/baeldung>) [![](assets/2026-06-25-Markdown%20Rendering%20Using%20commonmark-java/6af7991c4c6f5641c538d61a5608fb0b_MD5.png)](<https://feeds.feedblitz.com/_/29/958199054/baeldung,https%3a%2f%2fwww.baeldung.com%2fwp-content%2fuploads%2f2024%2f07%2fJava-Featured-10-1024x536.jpg>) [![](assets/2026-06-25-Markdown%20Rendering%20Using%20commonmark-java/533f73c805dddfc4d23114fef4ac7205_MD5.png)](<https://feeds.feedblitz.com/_/24/958199054/baeldung>) [![](assets/2026-06-25-Markdown%20Rendering%20Using%20commonmark-java/0130cc048dca99e29c926804679b6308_MD5.png)](<https://feeds.feedblitz.com/_/19/958199054/baeldung>) [![](assets/2026-06-25-Markdown%20Rendering%20Using%20commonmark-java/a12966c8b8df527e61bbaa696ddbdf28_MD5.png)](<https://feeds.feedblitz.com/_/20/958199054/baeldung>) [![](assets/2026-06-25-Markdown%20Rendering%20Using%20commonmark-java/a0674e7cd29f2bb749a6b32c7acdbbda_MD5.png)](<https://www.baeldung.com/java-commonmark-render-markdown#respond> "View Comments") [![](assets/2026-06-25-Markdown%20Rendering%20Using%20commonmark-java/074e9c5c0cc83cd9f21c55921090b857_MD5.png)](<https://www.baeldung.com/java-commonmark-render-markdown/feed> "Follow Comments via RSS")


---
> 原文链接: https://feeds.feedblitz.com/~/958199054/0/baeldung