#ifndef ABOUTPDANALYZERDIALOG_H
#define ABOUTPDANALYZERDIALOG_H

#include <QDialog>

namespace Ui {
class aboutPdAnalyzerDialog;
}

class aboutPdAnalyzerDialog : public QDialog
{
    Q_OBJECT

public:
    explicit aboutPdAnalyzerDialog(QWidget *parent = 0);
    ~aboutPdAnalyzerDialog();

private slots:
    void on_exitAboutButton_clicked();

private:
    Ui::aboutPdAnalyzerDialog *ui;
};

#endif // ABOUTPDANALYZERDIALOG_H
