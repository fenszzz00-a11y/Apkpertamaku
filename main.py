from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class AplikasiPertamaku(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.teks = Label(text='Halo! Ini aplikasi pertamaku', font_size=24)
        tombol = Button(text='KLIK AKU!', font_size=20, size_hint=(1, 0.3))
        tombol.bind(on_press=self.ganti_teks)
        layout.add_widget(self.teks)
        layout.add_widget(tombol)
        return layout

    def ganti_teks(self, instance):
        self.teks.text = 'Wah, berhasil! Kamu hebat!'

if __name__ == '__main__':
    AplikasiPertamaku().run()
  
