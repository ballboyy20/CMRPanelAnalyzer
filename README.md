
# CMRPanelAnalyzer
Jake and Trevor are re-writing some awesome code that Trevor wrote. It will take in RAW STLs and analyze them.

If you want to run the test files go read the README in the test folder

Dependicies 
    -pyvista
    -pyransac3d
    -numpy
    -pytest
    -pymesh - (are we actually using this? )


features surrounded by ## hashtags ## are optional/extra and could be implemented after basic functionality

Desired GUI Features:
    - Recognize provided file for one 3d object of type .stl ## or .obj, pointcloud ##
    - Give number of panels, then visualize and verify success of groupings
    - Give option to save unlabled groupings as a .json file ## or .csv, .xlsx, etc. ##
    - Give option to label and confirm labeling of this one array's panels from:
        - the provided 3d object file being processed
        - OR a provided link to a .json file ## or .csv, .xlsx, etc. ##
    - Give option to save this array's labeled panels as a new .json
    - Give option to extend labels to similar panels in a provided directory,
        plus visualizing and verifying the labels for all of the new panels,
        then save them ( to a new directory | with new names in the same directory)
    - Give option to analyze panels in comparison to each other from:
        - the provided 3d object file being processed
        - OR a provided link to a .json file ## or .csv, .xlsx, etc. ##
        When the file has been recognized, use these methods to analyze all panels of a single array:
        - mean and standard deviation of panel normal vectors
        - maximal deviation of panel normal vectors
        - out of plane alignment of panel centroids ## accounting for the out of plane translation that
            might be possible because of xy shift, more dramatically for panels with dramatically inclined normals
        Use these methods to analyze panels within a single array, ( using a visual interface | providing panel names ) to select panels:
        - all of the above methods for all panels relative to a ground panel
        - ## all of the above methods for some selected subgroup ##
        - ## all of the above methods for some selected subgroup relative to a ground panel ##
        - for two given panels, the absolute angle in space between their normals 
        - for two given panels, the euler angles in space between their normals relative to the first panel
        - for two given panels, the hingewise positions (theta_x, theta_y, delta_z) relative to the first,
            assuming a hinge equi-distant from both centroids and perpendicular to the line between the centroids
        - ## for two given panels, the hingewise positions (theta_x, theta_y, delta_z) relative to the first,
            ( operating by provided data about the position and orientation of the hinge relative to the two
            | operating by data in a .svg file that is aligned to match the panel, where lines represent hinges ) ##
        Use these methods to analyze a collection of panels from a directory and find:
        - the mean and standard deviation accross results from each array
        - the maximal deviations across results from all arrays
        - the mean and standard deviation of the normal and the centroid for each identically named panel across all arrays
        Save the results as:
        - .csv ## or .tsv ##
        - .xlsx
        - .xml
        - .txt
        - .parquet
        - .yaml
        - .json


Class panel
    attributes
        name
        normal
        centriod
        Hopefully some how well get the orientation of a 3D axis coordinate system
    methods
        getters
        setters
        what else??

class entire array
    attributes
        list of panels
        amounts of panels in the list
        what else??
    methods
        comparing panels (this will evolve into lots of methods)
        add panel to the list
        create a panel from json
        create panels from group (group is from scan class)
        create json
        read json

class scan 
    attributes
        Point cloud data
    mehtods
        create groups
        give the groups to entire array
        emliminate outliars


