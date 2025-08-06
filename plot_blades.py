# state file generated using paraview version 5.13.1
import paraview
import numpy as np
paraview.compatibility.major = 5
paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
D    = 126
H    = 90
xlen = 15*D
ylen = 3 *D
zlen = 3 *D
renderView1 = CreateView('RenderView')
renderView1.ViewSize                  = [1920, 1080]
renderView1.AxesGrid                  = 'Grid Axes 3D Actor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType                = 'Crystal Eyes'
renderView1.CameraFocalDisk           = 1.0
renderView1.LegendGrid                = 'Legend Grid Actor'
renderView1.PolarGrid                 = 'Polar Grid Actor'
renderView1.BackEnd                   = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary     = materialLibrary1
renderView1.CameraViewUp              = [0  , 0     , 1]
renderView1.CenterOfRotation          = [5*D, ylen/2, H]
renderView1.CameraFocalPoint          = [5*D, ylen/2, H]
renderView1.CameraPosition            = [0  ,-2*D   , H]
renderView1.CameraParallelScale       = 5*D

SetViewProperties(Background=[0.02, 0.02, 0.02], UseColorPaletteForBackground=0, view=renderView1)

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 1)
layout1.AssignView(1, renderView1)
layout1.SetSize(1920, 1080)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
disk_00000000nc = NetCDFReader(registrationName='test_00000000.nc*', FileName=[f"/lustre/orion/stf006/scratch/imn/turbine_viz/blades/test_{i:08d}.nc" for i in range(751)])
disk_00000000nc.Dimensions = '(z, y, x)'
disk_00000000nc.SphericalCoordinates = 0

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=disk_00000000nc)
calculator1.ResultArrayName = 'velocity'
calculator1.Function = 'uvel*iHat+vvel*jHat+wvel*kHat'

# create a new 'Gradient'
gradient1 = Gradient(registrationName='Gradient1', Input=calculator1)
gradient1.ScalarArray = ['POINTS', 'velocity']
gradient1.ComputeGradient = 0
gradient1.ComputeQCriterion = 1

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=gradient1)
contour1.ContourBy = ['POINTS', 'Q Criterion']
contour1.Isosurfaces = [0.3]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'velocity'
velocityTF2D = GetTransferFunction2D('velocity')
velocityTF2D.ScalarRangeInitialized = 1
velocityTF2D.Range = [4.0, 13.0, 0.0, 1.0]

# get color transfer function/color map for 'velocity'
velocityLUT = GetColorTransferFunction('velocity')
velocityLUT.TransferFunction2D = velocityTF2D
# print(GetLookupTableNames())
lut = GetColorTransferFunction('velocity')
lut.ApplyPreset('bone_Matlab', True)
dct = lut.SMProxy.GetClientSideObject()
mn = 3
mx = 13
dx = 0.1
tab = []
for x in np.arange(mn,mx,dx) :
    tab.append( x )
    tab.append( dct.GetRedValue  ((x-mn)/(mx-mn)) )
    tab.append( dct.GetGreenValue((x-mn)/(mx-mn)) )
    tab.append( dct.GetBlueValue ((x-mn)/(mx-mn)) )
velocityLUT.RGBPoints = tab
velocityLUT.ColorSpace = 'Lab'
velocityLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'velocity']
contour1Display.LookupTable = velocityLUT
contour1Display.Specular = 1.0
contour1Display.SpecularPower = 20.0
contour1Display.Ambient = 0.2
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.SelectTCoordArray = 'None'
contour1Display.TextureTransform = 'Transform2'
contour1Display.OSPRayScaleArray = 'Q Criterion'
contour1Display.OSPRayScaleFunction = 'Piecewise Function'
contour1Display.Assembly = ''
contour1Display.SelectedBlockSelectors = ['']
contour1Display.SelectOrientationVectors = 'velocity'
contour1Display.ScaleFactor = 80.23775329589844
contour1Display.SelectScaleArray = 'Q Criterion'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'Q Criterion'
contour1Display.GaussianRadius = 4.011887664794922
contour1Display.SetScaleArray = ['POINTS', 'Q Criterion']
contour1Display.ScaleTransferFunction = 'Piecewise Function'
contour1Display.OpacityArray = ['POINTS', 'Q Criterion']
contour1Display.OpacityTransferFunction = 'Piecewise Function'
contour1Display.DataAxesGrid = 'Grid Axes Representation'
contour1Display.PolarAxes = 'Polar Axes Representation'
contour1Display.SelectInputVectors = ['POINTS', 'velocity']
contour1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [0.003000000026077032, 0.0, 0.5, 0.0, 0.003000476863235235, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.003000000026077032, 0.0, 0.5, 0.0, 0.003000476863235235, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = GetOpacityTransferFunction('velocity')
velocityPWF.Points = [4.0, 0.0, 0.5, 0.0, 13.0, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = [renderView1]
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 750.0
animationScene1.EndTime = 750.0
animationScene1.PlayMode = 'Snap To TimeSteps'

# initialize the animation scene

# ----------------------------------------------------------------
# restore active source
SetActiveSource(contour1)
# ----------------------------------------------------------------

# SaveScreenshot('output_screenshot.png',
#                view=renderView1       ,
#                magnification=1        ,
#                quality=100            )

SaveAnimation('blades_animation.png', renderView1,
                  ImageResolution=[1920, 1080], # Specify desired resolution
                  FrameRate=30, # Frames per second for the animation
                  CompressionLevel=1) # PNG compression level (0-9)

##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
