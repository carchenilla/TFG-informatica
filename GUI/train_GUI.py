# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'training_design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
# Translated to PyQt5 UI by me
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_TFG(object):
    def setupUi(self, TFG):
        TFG.setObjectName(_fromUtf8("TFG"))
        TFG.resize(758, 572)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TFG.sizePolicy().hasHeightForWidth())
        TFG.setSizePolicy(sizePolicy)
        self.text_window = QtWidgets.QTextEdit(TFG)
        self.text_window.setGeometry(QtCore.QRect(40, 360, 681, 191))
        self.text_window.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.text_window.setObjectName(_fromUtf8("text_window"))
        self.clusterWidget = QtWidgets.QTabWidget(TFG)
        self.clusterWidget.setGeometry(QtCore.QRect(40, 20, 241, 231))
        self.clusterWidget.setObjectName(_fromUtf8("clusterWidget"))
        self.kmeans_tab = QtWidgets.QWidget()
        self.kmeans_tab.setObjectName(_fromUtf8("kmeans_tab"))
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.kmeans_tab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 0, 211, 71))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.kmeans_iters_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.kmeans_iters_line.setObjectName(_fromUtf8("kmeans_iters_line"))
        self.horizontalLayout_3.addWidget(self.kmeans_iters_line)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.kmeans_tab)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 40, 211, 71))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.kmeans_times_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.kmeans_times_line.setObjectName(_fromUtf8("kmeans_times_line"))
        self.horizontalLayout_4.addWidget(self.kmeans_times_line)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.kmeans_tab)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 80, 211, 71))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.kmeans_k_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.kmeans_k_line.setObjectName(_fromUtf8("kmeans_k_line"))
        self.horizontalLayout_5.addWidget(self.kmeans_k_line)
        self.kmeansbutton = QtWidgets.QPushButton(self.kmeans_tab)
        self.kmeansbutton.setGeometry(QtCore.QRect(130, 160, 91, 31))
        self.kmeansbutton.setObjectName(_fromUtf8("kmeansbutton"))
        self.clusterWidget.addTab(self.kmeans_tab, _fromUtf8(""))
        self.hierarch_tab = QtWidgets.QWidget()
        self.hierarch_tab.setObjectName(_fromUtf8("hierarch_tab"))
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.hierarch_tab)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 0, 211, 71))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.hier_maxd_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.hier_maxd_line.setObjectName(_fromUtf8("hier_maxd_line"))
        self.horizontalLayout_7.addWidget(self.hier_maxd_line)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.hierarch_tab)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 40, 211, 71))
        self.horizontalLayoutWidget_9.setObjectName(_fromUtf8("horizontalLayoutWidget_9"))
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        self.hier_linkage_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        self.hier_linkage_box.setObjectName(_fromUtf8("hier_linkage_box"))
        self.hier_linkage_box.addItem(_fromUtf8(""))
        self.hier_linkage_box.addItem(_fromUtf8(""))
        self.hier_linkage_box.addItem(_fromUtf8(""))
        self.hier_linkage_box.addItem(_fromUtf8(""))
        self.hier_linkage_box.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.hier_linkage_box)
        self.hierarbutton = QtWidgets.QPushButton(self.hierarch_tab)
        self.hierarbutton.setGeometry(QtCore.QRect(130, 160, 91, 31))
        self.hierarbutton.setObjectName(_fromUtf8("hierarbutton"))
        self.clusterWidget.addTab(self.hierarch_tab, _fromUtf8(""))
        self.dbscan_tab = QtWidgets.QWidget()
        self.dbscan_tab.setObjectName(_fromUtf8("dbscan_tab"))
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.dbscan_tab)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 0, 211, 71))
        self.horizontalLayoutWidget_10.setObjectName(_fromUtf8("horizontalLayoutWidget_10"))
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_9.addWidget(self.label_10)
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.dbscan_eps_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.dbscan_eps_line.setObjectName(_fromUtf8("dbscan_eps_line"))
        self.horizontalLayout_9.addWidget(self.dbscan_eps_line)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.dbscan_tab)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(10, 40, 211, 71))
        self.horizontalLayoutWidget_11.setObjectName(_fromUtf8("horizontalLayoutWidget_11"))
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_10.addWidget(self.label_11)
        spacerItem5 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.dbscan_minpts_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_11)
        self.dbscan_minpts_line.setObjectName(_fromUtf8("dbscan_minpts_line"))
        self.horizontalLayout_10.addWidget(self.dbscan_minpts_line)
        self.dbscanbutton = QtWidgets.QPushButton(self.dbscan_tab)
        self.dbscanbutton.setGeometry(QtCore.QRect(130, 160, 91, 31))
        self.dbscanbutton.setObjectName(_fromUtf8("dbscanbutton"))
        self.clusterWidget.addTab(self.dbscan_tab, _fromUtf8(""))
        self.validateWidget = QtWidgets.QTabWidget(TFG)
        self.validateWidget.setGeometry(QtCore.QRect(300, 20, 241, 231))
        self.validateWidget.setObjectName(_fromUtf8("validateWidget"))
        self.knn_tab = QtWidgets.QWidget()
        self.knn_tab.setObjectName(_fromUtf8("knn_tab"))
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.knn_tab)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(10, 0, 211, 71))
        self.horizontalLayoutWidget_12.setObjectName(_fromUtf8("horizontalLayoutWidget_12"))
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_11.addWidget(self.label_12)
        spacerItem6 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.knn_n_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_12)
        self.knn_n_line.setObjectName(_fromUtf8("knn_n_line"))
        self.horizontalLayout_11.addWidget(self.knn_n_line)
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.knn_tab)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(10, 40, 211, 71))
        self.horizontalLayoutWidget_13.setObjectName(_fromUtf8("horizontalLayoutWidget_13"))
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_13)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_12.addWidget(self.label_13)
        spacerItem7 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.knn_perc_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_13)
        self.knn_perc_line.setObjectName(_fromUtf8("knn_perc_line"))
        self.horizontalLayout_12.addWidget(self.knn_perc_line)
        self.knnbutton = QtWidgets.QPushButton(self.knn_tab)
        self.knnbutton.setGeometry(QtCore.QRect(120, 150, 101, 41))
        self.knnbutton.setObjectName(_fromUtf8("knnbutton"))
        self.validateWidget.addTab(self.knn_tab, _fromUtf8(""))
        self.svm_tab = QtWidgets.QWidget()
        self.svm_tab.setObjectName(_fromUtf8("svm_tab"))
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self.svm_tab)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(10, 0, 211, 71))
        self.horizontalLayoutWidget_14.setObjectName(_fromUtf8("horizontalLayoutWidget_14"))
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_13.addWidget(self.label_14)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.svm_kernel_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.svm_kernel_box.sizePolicy().hasHeightForWidth())
        self.svm_kernel_box.setSizePolicy(sizePolicy)
        self.svm_kernel_box.setObjectName(_fromUtf8("svm_kernel_box"))
        self.svm_kernel_box.addItem(_fromUtf8(""))
        self.svm_kernel_box.addItem(_fromUtf8(""))
        self.svm_kernel_box.addItem(_fromUtf8(""))
        self.svm_kernel_box.addItem(_fromUtf8(""))
        self.horizontalLayout_13.addWidget(self.svm_kernel_box)
        self.svm_button = QtWidgets.QPushButton(self.svm_tab)
        self.svm_button.setGeometry(QtCore.QRect(130, 160, 91, 31))
        self.svm_button.setObjectName(_fromUtf8("svm_button"))
        self.horizontalLayoutWidget_16 = QtWidgets.QWidget(self.svm_tab)
        self.horizontalLayoutWidget_16.setGeometry(QtCore.QRect(10, 80, 211, 71))
        self.horizontalLayoutWidget_16.setObjectName(_fromUtf8("horizontalLayoutWidget_16"))
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_16)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_15.addWidget(self.label_16)
        spacerItem9 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.svm_r_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_16)
        self.svm_r_line.setObjectName(_fromUtf8("svm_r_line"))
        self.horizontalLayout_15.addWidget(self.svm_r_line)
        spacerItem10 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_16)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_15.addWidget(self.label_17)
        self.svm_deg_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_16)
        self.svm_deg_line.setObjectName(_fromUtf8("svm_deg_line"))
        self.horizontalLayout_15.addWidget(self.svm_deg_line)
        self.label = QtWidgets.QLabel(self.svm_tab)
        self.label.setGeometry(QtCore.QRect(10, 130, 111, 41))
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayoutWidget_17 = QtWidgets.QWidget(self.svm_tab)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(10, 40, 211, 71))
        self.horizontalLayoutWidget_17.setObjectName(_fromUtf8("horizontalLayoutWidget_17"))
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_17)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_16.addWidget(self.label_19)
        spacerItem11 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem11)
        self.svm_gamma_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_17)
        self.svm_gamma_line.setObjectName(_fromUtf8("svm_gamma_line"))
        self.horizontalLayout_16.addWidget(self.svm_gamma_line)
        self.svm_perc_line = QtWidgets.QLineEdit(self.svm_tab)
        self.svm_perc_line.setGeometry(QtCore.QRect(10, 160, 81, 20))
        self.svm_perc_line.setObjectName(_fromUtf8("svm_perc_line"))
        self.validateWidget.addTab(self.svm_tab, _fromUtf8(""))
        self.years_tag = QtWidgets.QTabWidget(TFG)
        self.years_tag.setEnabled(True)
        self.years_tag.setGeometry(QtCore.QRect(560, 20, 161, 231))
        self.years_tag.setObjectName(_fromUtf8("years_tag"))
        self.train_years_tab = QtWidgets.QWidget()
        self.train_years_tab.setObjectName(_fromUtf8("train_years_tab"))
        self.gridLayoutWidget = QtWidgets.QWidget(self.train_years_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 160, 201))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.years_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.years_layout.setObjectName(_fromUtf8("years_layout"))
        self.check2002 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2002.setObjectName(_fromUtf8("check2002"))
        self.years_layout.addWidget(self.check2002, 0, 0, 1, 1)
        self.check2003 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2003.setObjectName(_fromUtf8("check2003"))
        self.years_layout.addWidget(self.check2003, 1, 0, 1, 1)
        self.check2004 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2004.setObjectName(_fromUtf8("check2004"))
        self.years_layout.addWidget(self.check2004, 2, 0, 1, 1)
        self.check2005 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2005.setObjectName(_fromUtf8("check2005"))
        self.years_layout.addWidget(self.check2005, 3, 0, 1, 1)
        self.check2006 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2006.setObjectName(_fromUtf8("check2006"))
        self.years_layout.addWidget(self.check2006, 4, 0, 1, 1)
        self.check2007 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2007.setObjectName(_fromUtf8("check2007"))
        self.years_layout.addWidget(self.check2007, 5, 0, 1, 1)
        self.check2008 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2008.setObjectName(_fromUtf8("check2008"))
        self.years_layout.addWidget(self.check2008, 6, 0, 1, 1)
        self.check2009 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2009.setObjectName(_fromUtf8("check2009"))
        self.years_layout.addWidget(self.check2009, 7, 0, 1, 1)
        self.check2011 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2011.setObjectName(_fromUtf8("check2011"))
        self.years_layout.addWidget(self.check2011, 1, 1, 1, 1)
        self.check2010 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2010.setObjectName(_fromUtf8("check2010"))
        self.years_layout.addWidget(self.check2010, 0, 1, 1, 1)
        self.check2012 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2012.setObjectName(_fromUtf8("check2012"))
        self.years_layout.addWidget(self.check2012, 2, 1, 1, 1)
        self.check2013 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2013.setObjectName(_fromUtf8("check2013"))
        self.years_layout.addWidget(self.check2013, 3, 1, 1, 1)
        self.check2014 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2014.setObjectName(_fromUtf8("check2014"))
        self.years_layout.addWidget(self.check2014, 4, 1, 1, 1)
        self.check2015 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2015.setObjectName(_fromUtf8("check2015"))
        self.years_layout.addWidget(self.check2015, 5, 1, 1, 1)
        self.check2016 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check2016.setObjectName(_fromUtf8("check2016"))
        self.years_layout.addWidget(self.check2016, 6, 1, 1, 1)
        self.checkAllbutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.checkAllbutton.setObjectName(_fromUtf8("checkAllbutton"))
        self.years_layout.addWidget(self.checkAllbutton, 7, 1, 1, 1)
        self.years_tag.addTab(self.train_years_tab, _fromUtf8(""))
        self.PCA_label = QtWidgets.QLabel(TFG)
        self.PCA_label.setGeometry(QtCore.QRect(40, 270, 201, 16))
        self.PCA_label.setObjectName(_fromUtf8("PCA_label"))
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(TFG)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 260, 160, 80))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.pca_box_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.pca_box_layout.setObjectName(_fromUtf8("pca_box_layout"))
        self.pca_box = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.pca_box.setObjectName(_fromUtf8("pca_box"))
        self.pca_box_layout.addWidget(self.pca_box)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(TFG)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(160, 260, 235, 78))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.pca_data_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.pca_data_layout.setObjectName(_fromUtf8("pca_data_layout"))
        self.dimension_layout = QtWidgets.QHBoxLayout()
        self.dimension_layout.setObjectName(_fromUtf8("dimension_layout"))
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dimension_layout.addWidget(self.label_2)
        self.dimension_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.dimension_edit.setObjectName(_fromUtf8("dimension_edit"))
        self.dimension_layout.addWidget(self.dimension_edit)
        self.pca_data_layout.addLayout(self.dimension_layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.threshold_edit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.threshold_edit_2.setText(_fromUtf8(""))
        self.threshold_edit_2.setObjectName(_fromUtf8("threshold_edit_2"))
        self.horizontalLayout.addWidget(self.threshold_edit_2)
        self.pca_data_layout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(TFG)
        self.pushButton.setGeometry(QtCore.QRect(599, 281, 121, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(TFG)
        self.clusterWidget.setCurrentIndex(0)
        self.validateWidget.setCurrentIndex(0)
        self.years_tag.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TFG)

    def retranslateUi(self, TFG):
        TFG.setWindowTitle(_translate("TFG", "TFG - Informática", None))
        self.label_3.setText(_translate("TFG", "Executions", None))
        self.kmeans_iters_line.setText(_translate("TFG", "100", None))
        self.label_5.setText(_translate("TFG", "Iterations", None))
        self.kmeans_times_line.setText(_translate("TFG", "6", None))
        self.label_6.setText(_translate("TFG", "No. of clusters", None))
        self.kmeans_k_line.setText(_translate("TFG", "4", None))
        self.kmeansbutton.setText(_translate("TFG", "Clusterize", None))
        self.clusterWidget.setTabText(self.clusterWidget.indexOf(self.kmeans_tab), _translate("TFG", "K-means", None))
        self.label_8.setText(_translate("TFG", "Max distance", None))
        self.hier_maxd_line.setText(_translate("TFG", "150", None))
        self.label_9.setText(_translate("TFG", "Linkage criteria", None))
        self.hier_linkage_box.setItemText(0, _translate("TFG", "ward", None))
        self.hier_linkage_box.setItemText(1, _translate("TFG", "single", None))
        self.hier_linkage_box.setItemText(2, _translate("TFG", "complete", None))
        self.hier_linkage_box.setItemText(3, _translate("TFG", "average", None))
        self.hier_linkage_box.setItemText(4, _translate("TFG", "weighted", None))
        self.hierarbutton.setText(_translate("TFG", "Clusterize", None))
        self.clusterWidget.setTabText(self.clusterWidget.indexOf(self.hierarch_tab), _translate("TFG", "Hierarchical", None))
        self.label_10.setText(_translate("TFG", "Epsilon", None))
        self.dbscan_eps_line.setText(_translate("TFG", "0.004", None))
        self.label_11.setText(_translate("TFG", "Min_Pts", None))
        self.dbscan_minpts_line.setText(_translate("TFG", "2692", None))
        self.dbscanbutton.setText(_translate("TFG", "Clusterize", None))
        self.clusterWidget.setTabText(self.clusterWidget.indexOf(self.dbscan_tab), _translate("TFG", "DBSCAN", None))
        self.label_12.setText(_translate("TFG", "No. of neighbors", None))
        self.knn_n_line.setText(_translate("TFG", "4", None))
        self.label_13.setText(_translate("TFG", "% of set for training", None))
        self.knn_perc_line.setText(_translate("TFG", "80", None))
        self.knnbutton.setText(_translate("TFG", "Train set \n"
" and validate", None))
        self.validateWidget.setTabText(self.validateWidget.indexOf(self.knn_tab), _translate("TFG", "K-nn", None))
        self.label_14.setText(_translate("TFG", "Kernel", None))
        self.svm_kernel_box.setItemText(0, _translate("TFG", "rbf", None))
        self.svm_kernel_box.setItemText(1, _translate("TFG", "linear", None))
        self.svm_kernel_box.setItemText(2, _translate("TFG", "poly", None))
        self.svm_kernel_box.setItemText(3, _translate("TFG", "sigmoid", None))
        self.svm_button.setText(_translate("TFG", "Train set \n"
" and validate", None))
        self.label_16.setText(_translate("TFG", "r", None))
        self.svm_r_line.setText(_translate("TFG", "0.0", None))
        self.label_17.setText(_translate("TFG", "degree", None))
        self.svm_deg_line.setText(_translate("TFG", "3", None))
        self.label.setText(_translate("TFG", "% of set for training", None))
        self.label_19.setText(_translate("TFG", "gamma", None))
        self.svm_gamma_line.setText(_translate("TFG", "0.125", None))
        self.svm_perc_line.setText(_translate("TFG", "80", None))
        self.validateWidget.setTabText(self.validateWidget.indexOf(self.svm_tab), _translate("TFG", "SVM", None))
        self.check2002.setText(_translate("TFG", "~2002", None))
        self.check2003.setText(_translate("TFG", "2003", None))
        self.check2004.setText(_translate("TFG", "2004", None))
        self.check2005.setText(_translate("TFG", "2005", None))
        self.check2006.setText(_translate("TFG", "2006", None))
        self.check2007.setText(_translate("TFG", "2007", None))
        self.check2008.setText(_translate("TFG", "2008", None))
        self.check2009.setText(_translate("TFG", "2009", None))
        self.check2011.setText(_translate("TFG", "2011", None))
        self.check2010.setText(_translate("TFG", "2010", None))
        self.check2012.setText(_translate("TFG", "2012", None))
        self.check2013.setText(_translate("TFG", "2013", None))
        self.check2014.setText(_translate("TFG", "2014", None))
        self.check2015.setText(_translate("TFG", "2015", None))
        self.check2016.setText(_translate("TFG", "2016", None))
        self.checkAllbutton.setText(_translate("TFG", "Check all", None))
        self.years_tag.setTabText(self.years_tag.indexOf(self.train_years_tab), _translate("TFG", "Train years", None))
        self.PCA_label.setText(_translate("TFG", "Principal Component Analysis", None))
        self.pca_box.setText(_translate("TFG", "Use PCA", None))
        self.label_2.setText(_translate("TFG", "Dimension:", None))
        self.label_4.setText(_translate("TFG", "Threshold:", None))
        self.pushButton.setText(_translate("TFG", "Update selected\n"
"dictionaries", None))

