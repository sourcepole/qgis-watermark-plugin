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

import resources

from watermark_plugin_layer import *
from watermark_plugin_layer_type import *

class WatermarkPlugin:

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface

  def initGui(self):
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(":/plugins/watermark/icon.png"), "Add watermark", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("triggered()"), self.run)

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("Watermark", self.action)

    # Register plugin layer type
    QgsPluginLayerRegistry.instance().addPluginLayerType(WatermarkPluginLayerType())

  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("Watermark",self.action)
    self.iface.removeToolBarIcon(self.action)

    # Unregister plugin layer type
    QgsPluginLayerRegistry.instance().removePluginLayerType(WatermarkPluginLayer.LAYER_TYPE)

  def run(self):
    # Create and add plugin layer
    layer = WatermarkPluginLayer()
    layer.showImageDialog()
    if layer.isValid():
      QgsMapLayerRegistry.instance().addMapLayer(layer)
