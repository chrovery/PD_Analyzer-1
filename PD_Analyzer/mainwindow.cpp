#include <QFileDialog>
#include <QMessageBox>

#include <QDebug>

#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "aboutpdanalyzerdialog.h"
#include "ui_aboutpdanalyzerdialog.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);


}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actionAbout_PD_Analyzer_triggered()
{
    aboutPdAnalyzerDialog* pwin = new aboutPdAnalyzerDialog();
    pwin->show();
    pwin->exec();
}

void MainWindow::on_actionOpen_triggered()
{
    QString path = QFileDialog::getOpenFileName(this, tr("Open PD data"), ".", tr("PD Files(*.pd)"));
    if(path.length() == 0)
    {
        QMessageBox::information(NULL, tr("Warning"), tr("You didn't select any files."));
    }
    else
    {
//        QMessageBox::information(NULL, tr("Path"), tr("You selected ") + path);
    }
}

void MainWindow::on_actionConnect_triggered()
{


}
