#include "aboutpdanalyzerdialog.h"
#include "ui_aboutpdanalyzerdialog.h"

aboutPdAnalyzerDialog::aboutPdAnalyzerDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::aboutPdAnalyzerDialog)
{
    ui->setupUi(this);
}

aboutPdAnalyzerDialog::~aboutPdAnalyzerDialog()
{
    delete ui;
}

void aboutPdAnalyzerDialog::on_exitAboutButton_clicked()
{
    this->close();
}
