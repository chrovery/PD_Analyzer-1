#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include <QtSerialPort/QSerialPort>
#include <QtSerialPort/QSerialPortInfo>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_actionAbout_PD_Analyzer_triggered();

    void on_actionOpen_triggered();

    void on_actionConnect_triggered();

private:
    Ui::MainWindow *ui;
    QSerialPort *my_serialPort;


};

#endif // MAINWINDOW_H
