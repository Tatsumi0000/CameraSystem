"""
@file: Bluetooth.py
@author: Tatsumi0000, Futa HIRAKOBA
@brief: EV3とBluetooth通信をする
"""
import serial
import random
import time


class Bluetooth:
    def __init__(self):
        """コンストラクタ
        """
        self.ser = serial.Serial()
        # ポートが開いていたら一旦閉じる．開いているのに開こうとするとだめなので．
        if self.ser.is_open:
            self.ser.close()

    def connect(self, port, baud=115200, timeout=5):
        """
        接続する

        :param port: str
            接続するポート番号
        :param baud: int
            ボーレート（デフォルトは115200）
        :param timeout: int
            タイムアウトの時間（単位は秒）
        """
        self.ser.port = port
        self.ser.baudrate = baud
        self.ser.timeout = timeout

        # 接続していない場合
        print("BT: ちょいまちこ")
        while not self.ser.is_open:
            try:
                self.ser.open()
            except serial.SerialException:
                # print("すこし待ってね⊂二二二（ ＾ω＾）二⊃ﾌﾞｰﾝ")
                time.sleep(3)  # 3秒後に接続リトライ
                continue
            except Exception:
                raise Exception("BT: 接続失敗m9(^Д^)ﾌﾟｷﾞｬｰ")

        print("BT: 接続成功ｷﾀ——(ﾟ∀ﾟ)——!!")

    def read(self):
        """
        シリアル通信でデータを受け取るメソッド
        :return: 受け取ったデータ
        """
        return int.from_bytes(self.ser.read(), 'big')

    def write(self, int_value, is_print=True):
        """
        シリアル通信でデータを送るメソッド
        :param int_value: int
        :param is_print: bool
            送るデータ
        """
        if is_print:
            print(f'{chr(int_value)}({int_value})を送信')
        self.ser.write(self.convert_to_byte(int_value, 1, "big"))

    @staticmethod
    def convert_to_byte(convert_data, byte_size, byte_order):
        """
        バイト変換を楽にするメソッド

        :param convert_data: int
            変換するデータ
        :param byte_size: int
            変換するバイトサイズ
        :param byte_order:
            バイトオーダー（ビッグエンディアンかリトルエンディアン）
        :return: 変換したやつ
        """
        return convert_data.to_bytes(byte_size, byte_order)


if __name__ == '__main__':
    bluetooth = Bluetooth()
    bluetooth.connect("/dev/cu.MindstormsEV3-SerialPor")
    while True:
        write_data = random.randint(0, 9)
        bluetooth.write(write_data)
        print(bluetooth.read())
        time.sleep(3)  # sec
