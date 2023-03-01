from numpy import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, \
    QHBoxLayout, QVBoxLayout, QFormLayout,QTableWidget, QTableWidgetItem, QGroupBox,QSpinBox,\
    QProgressBar
from time import *

app = QApplication([])
notes_win = QWidget()
bar = QProgressBar()
bar.setGeometry(0,0,100,50)
bar.setMinimum(0)
bar.setMaximum(999)
notes_win.arra = []
notes_win.arra1 = []
notes_win.text1 = ""
notes_win.text2 = ""

def vivod2():
    textW1.setText("")
    textW1.setText(notes_win.text1)
    textW1.append("__________________________________________")
    c = spin.value() - 1
    # all_time_w_ex, all_time_w_bu, time_repair_all, del_money_ex, del_money_bu, zp, plus_ex, plus_bu, smena_r_ex, smena_r_bu, smena_p_ex, smena_p_bu
    textW1.append("Рабочие часы машин: "+ str(notes_win.arra[c][0])+" "+str(notes_win.arra[c][1]))
    textW1.append("Суммарная длительность ремонта в часах: " + str(round(notes_win.arra[c][8]/3600,1)) + " " + str(round(notes_win.arra[c][9]/3600,1)))
    textW1.append("Простои в часах машин: " + str(round(notes_win.arra[c][10]/3600,1)) + " " + str(round(notes_win.arra[c][11]/3600,1)))
    textW1.append("рабочие часы слесарей: "+ str(notes_win.arra[c][2]))
    textW1.append("Убытки от простоя excavator: "+ str(notes_win.arra[c][3]))
    textW1.append("Убытки от простоя buldozer: "+ str(notes_win.arra[c][4]))
    textW1.append("Зарплата рабочих: "+ str(notes_win.arra[c][5]))
    textW1.append("Прибыль от работы excavator: "+ str(notes_win.arra[c][6]))
    textW1.append("Прибыль от работы buldozer: "+ str(notes_win.arra[c][7]))
    textW1.append("Итого прибыль: "+ str(notes_win.arra[c][7]+notes_win.arra[c][6]-notes_win.arra[c][5]-notes_win.arra[c][4]-notes_win.arra[c][3]))

    textW2.setText("")
    textW2.setText(notes_win.text2)
    textW2.append("__________________________________________")
    textW2.append("Рабочие часы машин: "+ str(notes_win.arra1[c][0])+" "+str(notes_win.arra1[c][1]))
    textW2.append("Суммарная длительность ремонта в часах: " + str(round(notes_win.arra1[c][8]/3600,1)) + " " + str(round(notes_win.arra1[c][9]/3600,1)))
    textW2.append("Простои в часах машин: " + str(round(notes_win.arra1[c][10]/3600,1)) + " " + str(round(notes_win.arra1[c][11]/3600,1)))
    textW2.append("рабочие часы слесарей: "+ str(notes_win.arra1[c][2]))
    textW2.append("Убытки от простоя excavator: "+ str(notes_win.arra1[c][3]))
    textW2.append("Убытки от простоя buldozer: "+ str(notes_win.arra1[c][4]))
    textW2.append("Зарплата рабочих: "+ str(notes_win.arra1[c][5]))
    textW2.append("Прибыль от работы excavator: "+ str(notes_win.arra1[c][6]))
    textW2.append("Прибыль от работы buldozer: "+ str(notes_win.arra1[c][7]))
    textW2.append("Итого прибыль: "+ str(notes_win.arra1[c][7]+notes_win.arra1[c][6]-notes_win.arra1[c][5]-notes_win.arra1[c][4]-notes_win.arra1[c][3]))


def vivod():
    notes_win.arra = []
    notes_win.arra1 = []
    bar.show()
    button2.setEnabled(False)
    button.setEnabled(False)
    for a in range(2):

        smena_p_ex = 0
        smena_p_bu = 0

        smena_r_ex = 0
        smena_r_bu = 0

        time_r_ex = 0
        time_r_bu = 0

        out_ex = 500
        out_bu = 300

        in_ex = 500
        in_bu = 300

        out_s6 = 100
        out_s3s5 = 160

        total = 0

        out_all  = 50

        math_ex_s6 = 1
        math_bu_s6 = 2
        math_ex_s3s6 = 0.25
        math_bu_s3s6 = 1.5


        time_w_ex = round(float(random.exponential(4))*3600,0)
        change_ex = time_w_ex

        time_w_bu = round(float(random.exponential(6))*3600,0)
        change_bu = time_w_bu

        status_ex = 1
        status_bu = 1

        status_of_w = 0 # не работает работник 0, работает 1

        math_ex = 0
        math_bu = 0
        mnoj = 0

        if a == 0:
            math_ex = math_ex_s6
            math_bu = math_bu_s6
            mnoj = out_s6
        elif a == 1:
            math_ex = math_ex_s3s6
            math_bu = math_bu_s3s6
            mnoj = out_s3s5

        print("Данные обрабатываются")
        for j in range(1000):
            smena_p_ex = 0
            smena_p_bu = 0
            smena_r_ex = 0
            smena_r_bu = 0
            time_r_ex = 0
            time_r_bu = 0
            time_w_ex = 0
            time_w_bu = 0
            status_of_w = 0

            time_w_ex = round(float(random.exponential(4)) * 3600, 0)
            change_ex = time_w_ex
            time_w_bu = round(float(random.exponential(6)) * 3600, 0)
            change_bu = time_w_bu
            for i in range(16*3600):
                if i == change_bu or change_ex:
                    if i == 0:
                        status_ex = 1
                        status_bu = 1
                    if change_ex < change_bu:
                        if status_of_w == 1 and status_ex == 1:
                            status_ex = 0
                            smena_p_ex += (change_bu - change_ex)
                            change_ex += (change_bu - change_ex)
                        if i == change_ex:
                            if status_of_w == 0 and status_ex != 2:
                                status_ex = 2
                                time_r_ex = round(float(random.exponential(math_ex))*3600,0)
                                change_ex+=time_r_ex
                                smena_r_ex+=time_r_ex
                                status_of_w = 1
                            elif status_ex == 2 and status_of_w == 1:
                                status_ex = 1
                                status_of_w = 0
                                time_w_ex = round(float(random.exponential(4)) * 3600,0)
                                change_ex += time_w_ex
                    elif change_ex == change_bu:
                        if status_ex == 2:
                            status_ex = 1
                            status_of_w = 0
                            time_w_ex = round(float(random.exponential(4)) * 3600, 0)
                            change_ex += time_w_ex
                            status_bu = 2
                            time_r_bu = round(float(random.exponential(math_bu)) * 3600, 0)
                            change_bu += time_r_bu
                            smena_r_bu += time_r_bu
                            status_of_w = 1
                        elif status_bu == 2:
                            status_bu = 1
                            status_of_w = 0
                            time_w_bu = round(float(random.exponential(6)) * 3600, 0)
                            change_bu += time_w_bu
                            status_ex = 2
                            time_r_ex = round(float(random.exponential(math_ex)) * 3600, 0)
                            change_ex += time_r_ex
                            smena_r_ex += time_r_ex
                            status_of_w = 1
                    else:
                        if status_of_w == 1 and status_bu == 1:
                            status_bu = 0
                            smena_p_bu += (change_ex - change_bu)
                            change_bu += (change_ex - change_bu)
                        if i == change_bu:
                            if status_of_w == 0 and status_bu != 2:
                                status_bu = 2
                                time_r_bu = round(float(random.exponential(math_bu))*3600,0)
                                change_bu+=time_r_bu
                                smena_r_bu+=time_r_bu
                                status_of_w = 1
                            elif status_bu == 2 and status_of_w == 1:
                                status_bu = 1
                                status_of_w = 0
                                time_w_bu = round(float(random.exponential(6)) * 3600,0)
                                change_bu += time_w_bu


            all_time_w_ex = round((16*3600-(smena_p_ex+smena_r_ex))/3600,1)
            all_time_w_bu = round((16*3600-(smena_p_bu+smena_r_bu))/3600,1)
            time_s_ex = round((smena_p_ex+smena_r_ex)/3600,1)
            time_s_bu = round((smena_p_bu+smena_r_bu)/3600,1)
            time_repair_all = round((smena_r_ex+smena_r_bu)/3600,1)

            del_money_ex = time_s_ex*out_ex
            del_money_bu = time_s_bu*out_bu

            zp = time_repair_all*mnoj+time_repair_all*out_all

            plus_ex = all_time_w_ex*in_ex
            plus_bu = all_time_w_bu*in_bu
            dop = [all_time_w_ex,all_time_w_bu,time_repair_all,del_money_ex,del_money_bu,zp,plus_ex,plus_bu,smena_r_ex,smena_r_bu,smena_p_ex,smena_p_bu]

            total +=(plus_bu+plus_ex-zp-del_money_ex-del_money_bu)
            if a == 0:
                notes_win.arra.append(dop)
            elif a == 1:
                notes_win.arra1.append(dop)
            sleep(0.01)
            bar.setValue(j)
            QApplication.processEvents()
        if a == 0:
            str_total = str(total)
            textW1.setText("Всего прибыли за 1000 дней работы слесаря 6 разряда: "+str_total)
            notes_win.text1 = "Всего прибыли за 1000 дней работы слесаря 6 разряда: "+str_total
            print(1)
        elif a == 1:
            str_total = str(total)
            textW2.setText("Всего прибыли за 1000 дней дней работы слесарей 3 и 6 разрядов: "+str_total)
            notes_win.text2 = "Всего прибыли за 1000 дней дней работы слесарей 3 и 6 разрядов: "+str_total
            print(2)

    bar.setValue(0)
    bar.hide()
    button.setEnabled(True)
    button2.setEnabled(True)

gl_vertical_lay = QVBoxLayout()
lay1 = QVBoxLayout()
lay2 = QVBoxLayout()
layH = QHBoxLayout()
lay1GbV = QVBoxLayout()
group1 = QGroupBox()
label2 =QLabel("Мат. Ожидание для машин\nБульдозер - 6\nЭкскаватор - 4\nРаботают по 16 часов в день")




table = QTableWidget()
table.setColumnCount(3)
table.setRowCount(2)
table.setHorizontalHeaderLabels([" ", "Бульдозер", "Экскаватор"])
table.horizontalHeaderItem(0).setToolTip("Column 1 ")
table.horizontalHeaderItem(1).setToolTip("Column 2 ")
table.horizontalHeaderItem(2).setToolTip("Column 3 ")
table.setItem(0, 0, QTableWidgetItem("Слесарь 6 разряда"))
table.setItem(0, 1, QTableWidgetItem("2"))
table.setItem(0, 2, QTableWidgetItem("1"))
table.setItem(1, 0, QTableWidgetItem("Слесарь 6 разряда + Слесарь 3 разряда"))
table.setItem(1, 1, QTableWidgetItem("1.5"))
table.setItem(1, 2, QTableWidgetItem("0,25"))
table.resizeColumnsToContents()
table.setMaximumSize(500,110)

lable1 = QLabel("Мат. Ожидание для работников")


lay1.addWidget(lable1)
lay1.addWidget(table)
lay1.addStretch()
lay1.setAlignment(Qt.AlignTop)
lay2.addWidget(label2)
lay2.setAlignment(Qt.AlignTop)
layH.addLayout(lay1)
layH.addLayout(lay2)

layH2 = QHBoxLayout()
button = QPushButton("Запустить программу и вывести итоги")

gl_vertical_lay.addLayout(layH)


gl_vertical_lay.addWidget(button)
labellday = QLabel("Вывод данных определенного дня")
button2 = QPushButton("Вывести день")
spin = QSpinBox()
spin.setMinimumWidth(150)
spin.setMaximum(1000)
spin.setMinimum(1)

textW1 = QTextEdit()
textW2 = QTextEdit()
textWend = QTextEdit()
layh3 = QHBoxLayout()
layh3.addWidget(labellday)
layh3.addStretch()
layh3.addWidget(spin)
layh3.addWidget(button2)
layH2.addWidget(textW1)
layH2.addWidget(textW2)
gl_vertical_lay.addLayout(layh3)
gl_vertical_lay.addLayout(layH2)

button2.setEnabled(False)
gl_vertical_lay.addWidget(bar)
gl_vertical_lay.addStretch()

notes_win.setLayout(gl_vertical_lay)

notes_win.setWindowTitle('Домашняя работа')
notes_win.resize(900, 600)
textW1.setReadOnly(True)
textW2.setReadOnly(True)
bar.hide()
table.setEnabled(False)


button2.clicked.connect(vivod2)
button.clicked.connect(vivod)
notes_win.show()
app.exec_()











