# -*- coding: utf-8 -*-
"""
/***************************************************************************
Watermark Plugin
A QGIS plugin
Render watermark showing basic QgsPluginLayer usage

                             -------------------
begin                : 2010-01-28
copyright            : (C) 2010 by Sourcepole
email                : info at sourcepole dot ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from watermark_plugin_layer import *

class WatermarkPluginLayerType(QgsPluginLayerType):

  def __init__(self):
    QgsPluginLayerType.__init__(self, WatermarkPluginLayer.LAYER_TYPE)

  def createLayer(self):
    return WatermarkPluginLayer()

  def showLayerProperties(self, layer):
    layer.showImageDialog()

    # indicate that we have shown the properties dialog
    return True
