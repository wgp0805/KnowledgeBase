---
title: "AWS Image Builder Plugin for TeamCity"
source: "JetBrains Blog"
url: "https://blog.jetbrains.com/teamcity/2026/06/teamcity-aws-ami-builder/"
date: "Mon, 22 Jun 2026 12:17:43 +0000"
score: 0.95
tags: ["Java", "IDE", "工具", "Kotlin"]
auto_captured: true
---

# AWS Image Builder Plugin for TeamCity

> **来源**: JetBrains Blog  
> **链接**: https://blog.jetbrains.com/teamcity/2026/06/teamcity-aws-ami-builder/  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.95

Cloud build agents are one of those CI/CD features that feel almost magical when everything works well. Your TeamCity server can scale build capacity up when the queue gets busy, then wind it back down when the rush is over. You get extra power exactly when you need it, without keeping machines idle the rest of the time.

They also make builds cleaner and more predictable. Each cloud agent starts as a fresh VM from a cloud image, so every build gets an isolated environment rather than inheriting the state left behind by a previous build. Scalable, cost-efficient, and reliable, cloud build agents are a perfect fit for a truly robust and streamlined TeamCity setup.

Of course, cloud build agents are not without trade-offs. The most obvious one is maintenance. Agents are launched from a static machine image, and that image starts aging the moment your tooling changes or the TeamCity server is updated. Suddenly, every new agent has to spend valuable time catching up… or you have to repeat the familiar cycle: Start an instance, install updates, create a new snapshot, and update the TeamCity cloud profile.

Large repositories add another wrinkle. Since every cloud agent starts from a fresh VM, it also starts with an empty checkout directory. The bigger the repository, the more time each build can spend just pulling sources. One workaround is to bake repository mirrors into the image alongside your tools, so agents only need to fetch the latest commits. But that, too, is temporary: As changes accumulate, the mirrors become stale, and the image needs another update.

If you run AMI-based cloud build agents on Amazon Web Services, there’s a better way to handle this – the AWS Image Builder plugin. It turns image maintenance from a manual, repetitive chore into a regular TeamCity build configuration.

## Prerequisites

To automate AMI updates, download and install the [_AWS Image Builder_ TeamCity plugin](<https://plugins.jetbrains.com/plugin/31512-aws-image-builder>) from JetBrains Marketplace. You can do this directly in TeamCity: navigate to _Admin | Plugins_ , then click _Browse plugins repository_. Don’t forget to enable this plugin after installing it.

You will also need a suitable [AWS connection](<https://www.jetbrains.com/help/teamcity/configuring-connections.html#AmazonWebServices>) configured in TeamCity. The connection’s IAM principal needs EC2 permissions to launch instances, create images, and read VPC metadata.

# Create a build configuration

  1. Once the plugin is installed and enabled, [create a new build configuration](<https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html>) under the project that has access to the AWS connection mentioned in the previous section.
  2. Add the _Image Builder AWS AMI_**** build step.

![](assets/2026-06-25-AWS%20Image%20Builder%20Plugin%20for%20TeamCity/774bbf35d9a4549743cfaa3f91c43a63_MD5.png)

  3. Specify core step settings:


  * _AWS Connection_**** – Choose the connection that TeamCity will use to communicate with AWS.
  * _Base AMI_**** – Select the AMI this configuration will rebuild.
  * _Network settings_**** – Required to access AWS resources.
  * _Tags_ – The list of `name=value` tags that will be assigned to a newly built AMI. This step is important if you want TeamCity to automatically update its cloud profiles (see below).
  * _Image access_ – Enter account IDs, organization ARNs, or OU ARNs to specify who will be able to access your newly built image.


  4. Tick _Install TeamCity agent_**** to bake the build agent into the AMI. The full agent distribution will be taken directly from the TeamCity instance, so your agents will always match the server version. After major TeamCity updates, run this build configuration to supply your AMI with the corresponding agent version.
  5. Specify optional scripts to run during the build (TeamCity first-run script files; the inline script will be executed last). You can use these scripts to install runtimes, SDKs, agent plugins, or perform any environment setup that would otherwise run on every agent boot.
  6. Enable VCS mirrors to speed up the build checkout phase. The plugin will pre-populate the image with Git object mirrors based on the VCS roots attached to this configuration. The roots contain all the required information (connection details, credentials, submodule checkout policy, and so on), making them the perfect tool for the job.



To specify which mirrors should be baked in:

  * Save the build step to go back to the build configuration settings.
  * Navigate to the _Version Control_**** tab and click _Attach VCS Root_.
  * If your AMI builder configuration is owned by the same project that has regular configurations that build, test, and deploy required repositories, you can attach an existing VCS root. Otherwise, create a new one.
  * For a newly created Git VCS root, specify the fetch URL and authorization settings.
  * Switch the root’s _Checkout policy_**** to _Use mirrors_.



# Run the builder configuration

Once you’ve filled in all build-step and VCS root settings, run the configuration and verify the results.

  * Check the value of the `teamcity.build.awsImageBuilder.amiId` build parameter that stores the AMI ID of your new image.
  * Navigate to the _Artifacts_**** tab and view the hidden `.teamcity/image_builder/` artifact. This directory stores a generated [HashiCorp Packer template](<https://developer.hashicorp.com/packer/tutorials/aws-get-started/aws-get-started-build-image>) that the AWS Image Builder plugin uses to upload the final AMI.
  * Log in to your AWS console to verify the new AMI is published and tagged.

![](assets/2026-06-25-AWS%20Image%20Builder%20Plugin%20for%20TeamCity/54abdf992cd5087b268b6a1d1441335f_MD5.png)

# Update TeamCity cloud profiles

Building an updated AMI is only half the automation story. The next step is making sure TeamCity starts using it automatically as soon as it’s ready.

To do this, go to _Project settings | Cloud profiles_ , open the profile you want to update, and check each cloud image in it. Set the _Instance_ toggle to _AMI by tags_ so TeamCity selects images by tag instead of a fixed AMI ID. Use the same AMI tags that you configured in the image builder build step.

Over time, repeated image builder runs will produce multiple AMIs with the same tags, but that will not become an issue. When a cloud image uses the _AMI by tags_ policy, TeamCity periodically checks AWS for matching AMIs and chooses the one with the most recent creation date. This means your cloud agents can keep launching from the latest AMI without any manual profile updates.

# Kotlin DSL

If you prefer to configure your TeamCity workflows in [Kotlin DSL](<https://www.jetbrains.com/help/teamcity/kotlin-dsl.html>) rather than TeamCity UI, here’s how to configure the AMI builder step in code:
    
    
    awsImageBuilderBuild {
    
        name = "Build Agent AMI"
    
        awsConnectionId = "AmazonWebServicesAws"
    
        baseAmi = "ami-0xxxxxxxxxxxxxxxxx"
    
        instanceType = "t3.medium"
    
        subnetId = "subnet-0xxxxxxxxxxxxxxxxx"
    
        tags = """
    
            role=teamcity-agent
    
            env=prod
    
        """.trimIndent()
    
        includeAgent = true
    
        inlineScript = "systemctl enable teamcity-agent"
    
    }

# Tell us what you think

We love building features that solve real, everyday DevOps challenges. The AWS Image Builder plugin is designed to do exactly that by making cloud build agent maintenance much easier, so you can spend less time tinkering with the images and more looking at your builds.

As always, your feedback matters. If you run into issues or feel that an important customization option is missing, please let us know in the comments on the [JetBrains Marketplace plugin page](<https://plugins.jetbrains.com/plugin/31512-aws-image-builder>) or in the corresponding [YouTrack ticket](<https://youtrack.jetbrains.com/issue/TW-75387>).


---
> 原文链接: https://blog.jetbrains.com/teamcity/2026/06/teamcity-aws-ami-builder/