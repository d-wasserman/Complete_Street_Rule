# What is the Complete Street Rule?
Complete Streets is a robust procedural street example that incorporates knowledge and ideas from various sources of transportation planning knowledge including NACTO Design Guidelines, AASHTO Design Recommendations, and MUTCD standards. The goal of the rule is to represent a diversity of street configurations to support multimodal planning in urban areas, and provide some basis for before and after comparisons of street treatments and transportation investments in Esri CityEngine. Along with visualization, the street rule includes analytical reports on various aspects of the geometry of the street that can be used to inform rough cost estimates. In addition to these analytics, the street rule has various customizable thematics and reports that use information from the geometry and configuration of the street to suggest how it might impact the "stress levels" put on different modes. The street rule intends to represent transportation planning treatments for complete streets within urban areas and common highway configurations that might include shoulders, Jersey barriers, and HOV Lanes.
This is an updated repository for a modified version of the ESRI Complete Street rule by the original rule author.

## Scenario Oriented Design Tool

![alt tag](https://github.com/d-wasserman/Complete_Street_Rule/blob/master/images/CSRuleCEDemo.gif)


# Instructions
To open and interact with this project, do the following:
1.	Click Clone or Download > Download Zip above to download the project zip file to your computer.

2.	Unzip the repository folder in a selected workspace.

3.	Launch CityEngine.

4.	Locate the unzipped project folder and click Open.

5.	Keep the default settings and click Finish.

6.	Expand the imported project folder in Navigator window and click the scenes folder.

7.	Double click the .cej file to open the scene in CityEngine.

If all you need is the rule for your current project: 
1.	Click Clone or Download > Download Zip above to download the project zip file to your computer.

2.	Unzip the repository folder in a selected workspace.

3.	Go into the directory and find the "rules" and "assets" folder. 

4.	Move the Complete_Streets folder in assets to your current project's assets folder. 

5.	Move the files ending in .CGA in the rules folder to your current project's rules's folder. 

6.	Open CityEngine. 

7.	Apply rule to desired street segments.

![alt tag](https://github.com/d-wasserman/Complete_Street_Rule/blob/master/images/RoadDietEX.jpg)

# Key changes to the rule include:

1. Best Fit setting allows the rule to make sure that the street has the option to not have exact geometry.
This still needs to be tested more so please comment if you have any issues with the rule. The best fit feature works by calculating empty space and then adding it to the lane width. This means that your lane width attribute becomes the minimum width the lanes can take on before it subtracts lanes.

2. Renamed reporting and creates subclasses to support new Dashboards capabilities in all versions of CityEngine beyond 2015.2.  

3. Added Mode Area reporting and dashboards to the street rule. Get percentage area dedicated to each mode for different designs.

4. Improved Default LOD Settings: If LOD is set to High, the street will now pick default population parameters to make the street seem occupied. LOD Settings are now Low (Asset choice changes to reduce polygon count), Moderate (high polygon assets/choices), and High/Very High (high polygon assets and populated streets).

5. Addition of Complete_Street_Simple.CGA: This additional included rule has about ~50 fewer attributes while maintaining the core functionality of the rule. This rule is intended to make demos or charrettes a little easier.

6. Addition of Sharrows + Sidewalk Side Bike Lanes: Added support for sharrows (shared use lanes). The sharrows only appear on the curb lane. In addition to sharrows, sidewalk side bike lanes were added after a lot of international demand was declared for them. These lanes do not have buffers, but are placed between the planting and the walkway when bike lane type is set to "Sidewalk". 

7. Addition of Mode Focused Thematics: Allows a user to highlight specific improvements to a street with custom color choices. For example, if you add a bike lane and select "Bicycle Highlight" thematic, the solid color attribute will only highlight added bike lanes. Also, the addition of a All Mode Preference option helps visualize all the mode preference reports at once.  

8. Dimension Extrusion: This added option to the bridge settings enables single cross sectional images to have the mode categorization be shown at the street's edge. This provides a starting place for report infographics that denote different modes served by different treatments. 

9. Handles Support: Local Edits allow randomly generated and spaced assets to be moved within a CityEngine model rather than post processed in PhotoShop or some other 3D modeling software. Current assets and elements that can be edited with handles include: Street Lamps|Traffic Lights|Trees|Benches.

10. Curbside Management: There are changes to parallel parking that provide a template for how cities can reallocate curbspace to support micro-mobility (scooters/bikeshare/DoBi), transit operations, freight loading zones, and passenger drop off locations to support TNC/Taxi operations and in preparation for supporting shared autonomous vehicles. 

11. Other miscellaneous changes.

	-Dead end exception, dead ends, treated like they have a connection (for non-singular cross sections and shorter segments). 
	
	-Modal Preference replaced LTS to provide more clarity of what the metrics represent across modes. 

	-Fixed striping bug in right most lane that occurred as a result of floating point arithmetic/rounding error (a micro-lane is being created).

	-Fixed various aspects of the Bike Stress Ranking to deal with parking and cycle tracks.

	-Fixed how multimodal lanes handle non-intersections-the last stamps will not be added when they connect to joints and other "non-stop" neighbor shapes.

	-Better default planting widths for sidewalks: Sidewalk planting width was changed to mimic general guidelines and suggestions from a NACTO Tree Maintenance Guidelines Document. If you have a narrow sidewalk, the planting strip will narrow to a minimum of 2 feet, and grow to a maximum of 6 feet.

	-Furniture Zone Width Parameter was added to adjust the gap between the sidewalk and the curb. This parameter is set to small gap, but can be increased. 
	
	-Paint Reporting is removed from the rule. Feedback indicating it was slowing down the rule, and made editing the rule more difficult. 
