# Complete_Street_Rule
This is an updated repository for a modified version of the ESRI Complete Street rule by the original rule author. 
The rule uses the original assets folder of the ESRI Complete street rule, so in order to use it, you really only need the updated CGA file. 
# Instructions
To open and interact with this project, do the following:
1.	Click Clone or Download > Download Zip above to download the project zip file to your computer.
2.	Unzip the repository folder in a selected workspace.
3.	Launch CityEngine.
3.	Locate the unzipped project folder and click Open.
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

![alt tag](https://geonet.esri.com/servlet/JiveServlet/showImage/102-6915-27-160154/RoadDiet6.jpeg.jpg)
The rules new features include: 

Key changes to the rule include:

1. Best Fit setting allows the rule to make sure that the street has the option to not have exact geometry.
This still needs to be tested more so please comment if you have any issues with the rule. The best fit feature works by calculating empty space and then adding it to the lane width. This means that your lane width attribute becomes the minimum width the lanes can take on before it subtracts lanes.

2. Renamed reporting and creates subclasses to support new Dashboards in 2015.2. Sample Dashboard template included in project. 

3. Added Mode Area reporting and dashboards to the street rule. Get percentage area dedicated to each mode for different designs.

4. Improved Default LOD Settings: If LOD is set to High, the street will now pick default population parameters to make the street seem occupied. LOD Settings are now Low (Asset choice changes to reduce polygon count), Moderate (high poly assets/choices), and High (high poly assets and populated streets).

5. Addition of Complete_Street_Simple.CGA: This additional included rule has about ~50 fewer attributes while maintaining the core functionality of the rule. This rule is intended to make demos or charrettes a little easier.

6. Addition of Sharrows + Sidewalk Side Bike Lanes: Added support for sharrows (shared use lanes). The sharrows only appear on the curb lane. In addition to sharrows, sidewalk side bike lanes were added after a lot of international demand was declared for them. These lanes do not have buffers, but are placed between the planting and the walkway when bike lane type is set to "Sidewalk". 

7. Addition of Mode Focused Thematics: Allows a user to highlight specific improvements to a street with custom color choices. For example, if you add a bike lane and select "Bicycle Highlight" thematic, the solid color attribute will only highlight added bike lanes. Also, the addition of a All Mode Preference option helps visualize all the mode preference reports at once.  

8. Other miscellaneous changes.

	-Dead end exception, dead ends, treated like they have a connection (for singular cross sections).
	
	-Modal Preference replaced LTS to provide more clarity of what the metrics represent across modes. 

	-Fixed striping bug in right most lane that occurred as a result of floating point arithmetic/rounding error (a micro-lane is being created).

	-Fixed various aspects of the Bike Stress Ranking to deal with parking and cycle tracks.

	-Fixed how multimodal lanes handle non-intersections-the last stamps will not be added when they connect to joints and other "non-stop" neighbor shapes.

	-Better default planting widths for sidewalks: Sidewalk planting width was changed to mimic general guidelines and suggestions from a NACTO Tree Maintenance Guidelines Document. If you have a narrow sidewalk, the planting strip will narrow to a minimum of 2 feet, and grow to a maximum of 6 feet.
