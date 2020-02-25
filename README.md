# What is the Complete Street Rule?
Complete Streets is a robust procedural street example that incorporates knowledge and ideas from various sources of transportation planning guidance including NACTO Design Guidelines, AASHTO Design Recommendations, and MUTCD standards. The goal of the rule is to enable the 3D representation of a diversity of street configurations to support multimodal planning in urban areas, and provide some basis for before and after comparisons of street treatments and transportation investments in Esri CityEngine. Alongside being a quick response parametric visualization tool for streets, this street rule has dynamic performance metrics and reports that react to changes in a streets configuration and related parameters. These performance metrics provide a template for how procedural rules can create a responsive connection between design, metrics, and visualization that enables the rapid exploration and communication of different design scenarios. This street rule is well suited to representing transportation planning treatments for complete streets and common highway configurations that might include shoulders, jersey barriers, and HOV Lanes. By being a part of Esri CityEngine, the Complete Street Rule can create 3D models of streets that can be exported to different 3D formats,  scene layer packages to be shared over the web, and even exports compatible with game engines such as Unity & Unreal to create virtual experiences as part of public outreach efforts. 

This is an updated repository for a modified version of the ESRI Complete Street rule by the original rule author.

## Scenario Oriented Design Tool

![alt tag](/images/CSRuleCEDemo.gif)

# Instructions

If you are new to using CityEngine, then the instructions on this [page](Instructions.md) provide step by step instructions on how to open the project or integrate the rule into an existing project. 


# Key Features of the Complete Street Rule

* Enables Quick Visualization of Multiple Features of Complete Streets: The rule can be used to quickly iterate on high level cross-sectional designs for streets through changes to its parameters. The features that can be visualized include bike lanes, bike lane buffers, shared-use lanes, bus lanes, HOV lanes, parking lanes, medians, two-way left turn lanes, and sidewalks featuring trees, street furniture, and other amenities. 

* Dynamic Performance Metrics & Analytics: The Complete Street rule includes a diversity of reports that can be leveraged inside of CityEngine to power dynamic dashboards that react to changes to a street's configuration and design. The supported metrics include modal preference metrics such as level of traffic stress for bicyclists, metrics related to curbside allocations and parking space counts, metrics related to how much space on the street overall is allocated to different modes of transport, vegetation & impervious cover amounts, and speed related metrics.  

* Support for Curbside Management: The rule's options for parallel parking include options to reallocate curb space to other uses. These curbspace management options provide a template for how cities can reallocate curbspace to support micro-mobility (scooters/bikeshare/DoBi), transit operations, freight loading zones, and passenger drop-off locations to support TNC/Taxi operations and in preparation for supporting shared autonomous vehicles.

* Mode Focused Thematics: Allows a user to highlight specific improvements to a street with custom color choices. For example, if you add a bike lane and select "Bicycle Highlight" thematic, the solid color attribute will only highlight added bike lanes. Also, the addition of a All Mode Preference option helps visualize all the mode preference reports at once. There are also options for NACTO themed highlights of the street, and preliminary support for semantic highlighting for the purpose of supporting synthetic data generation for deep learning models. 

* CityeEngine Handles Support: Local Edits allow randomly generated and spaced assets to be moved within a CityEngine model rather than post processed in PhotoShop or some other 3D modeling software. Current assets and elements that can be edited with handles include: Street Lamps|Traffic Lights|Trees|Benches|Curbside Allocations.

* Support for Multiple Levels of Detail (LOD): If LOD is set to High, the street will now pick default population parameters to make the street seem occupied. LOD Settings are now Low (Asset choice changes to reduce polygon count), Moderate (high polygon assets/choices), and High/Very High (high polygon assets and populated streets).

![alt tag](/images/Road_Diet_Update.jpg)

# Citations
If you use the complete street rule in academic research or as part of professional reports, please cite the rule as the following: 

Wasserman, D. Complete Street Rule. (2019) GitHub repository, https://github.com/d-wasserman/Complete_Street_Rule.
