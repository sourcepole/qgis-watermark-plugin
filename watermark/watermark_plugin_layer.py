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

class WatermarkPluginLayer(QgsPluginLayer):

  LAYER_TYPE="watermark"

  def __init__(self):
    QgsPluginLayer.__init__(self, WatermarkPluginLayer.LAYER_TYPE, "Watermark plugin layer")
    self.setValid(True)

    self.image_path = "."
    self.image = None

  def draw(self, rendererContext):
    if self.image != None:
      painter = rendererContext.painter()
      extent = rendererContext.extent()
      mapToPixel = rendererContext.mapToPixel()
      rasterScaleFactor = rendererContext.rasterScaleFactor()
      invRasterScaleFactor = 1.0/rasterScaleFactor

      # get dimensions of painter area (so it is also correctly scaled in print composer)
      # Note: watermark is not correctly scaled in print preview
      topleft = mapToPixel.transform(extent.xMinimum(), extent.yMaximum())
      bottomright = mapToPixel.transform(extent.xMaximum(), extent.yMinimum())
      width = (bottomright.x() - topleft.x()) * rasterScaleFactor
      height = (bottomright.y() - topleft.y()) * rasterScaleFactor

      # setup painter
      painter.save()
      painter.scale(invRasterScaleFactor, invRasterScaleFactor)

      # render watermark image in lower left corner
      painter.setOpacity(0.5)
      y = height - 32 - self.image.height()
      painter.drawImage(32, y, self.image)

      painter.restore()
    return True

  def readXml(self, node):
    # custom properties
    self.readImage( node.toElement().attribute("image_path", ".") )
    return True

  def writeXml(self, node, doc):
    element = node.toElement();
    # write plugin layer type to project  (essential to be read from project)
    element.setAttribute("type", "plugin")
    element.setAttribute("name", WatermarkPluginLayer.LAYER_TYPE);
    # custom properties
    element.setAttribute("image_path", str(self.image_path))
    return True

  def readImage(self, image_path):
    self.image_path = image_path
    self.image = QImage(self.image_path)

  def showImageDialog(self):
    filename = QFileDialog.getOpenFileName(None, "Select watermark image", self.image_path, "Image Files (*.png *.jpg *.bmp)")
    if filename != "":
      self.readImage(filename)

      # trigger repaint
      self.setCacheImage(None)
      self.emit(SIGNAL("repaintRequested()"))
