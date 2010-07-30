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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
  return "Watermark Plugin"
def description():
  return "Render watermark using QgsPluginLayer"
def version():
  return "Version 1.0"
def qgisMinimumVersion():
  return "1.5"
def authorName():
  return "Sourcepole"
def homepage():
  return "http://github.com/sourcepole/qgis-watermark-plugin"
def classFactory(iface):
  from watermark_plugin import WatermarkPlugin
  return WatermarkPlugin(iface)
