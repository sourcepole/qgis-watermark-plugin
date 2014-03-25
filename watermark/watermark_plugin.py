# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WatermarkPlugin
                                 A QGIS plugin
 Render watermark using QgsPluginLayer
                              -------------------
        begin                : 2014-03-24
        copyright            : (C) 2014 by Sourcepole
        email                : info@sourcepole.ch
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
from watermark_plugin_layer import *
from watermark_plugin_layer_type import *
import os.path


class WatermarkPlugin:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'watermark_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/watermark/icon.png"), "Add watermark", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Watermark", self.action)

        # Register plugin layer type
        QgsPluginLayerRegistry.instance().addPluginLayerType(WatermarkPluginLayerType())

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("Watermark", self.action)
        self.iface.removeToolBarIcon(self.action)

        # Unregister plugin layer type
        QgsPluginLayerRegistry.instance().removePluginLayerType(WatermarkPluginLayer.LAYER_TYPE)

    def run(self):
        # Create and add plugin layer
        layer = WatermarkPluginLayer()
        layer.showImageDialog()
        if layer.isValid():
            QgsMapLayerRegistry.instance().addMapLayer(layer)
