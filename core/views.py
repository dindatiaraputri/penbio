
from django.shortcuts import render
from django.http import Http404


# ==================================================
# DATA MATERI PEMBELAJARAN SISTEM REPRODUKSI MANUSIA
# ==================================================

DAFTAR_MATERI = [

    # ==================================================
    # A. PENGERTIAN DAN FUNGSI SISTEM REPRODUKSI
    # ==================================================

    {
        "slug": "pengertian-sistem-reproduksi",
        "kode": "A",
        "judul": "Pengertian dan Fungsi Sistem Reproduksi Manusia",
        "deskripsi": "Mengenal pengertian, tujuan, fungsi, serta peran sistem reproduksi dalam kehidupan manusia.",
        "gambar": "img/materi/Gambar 1. Gambaran umum sistem reproduksi laki-laki..jpeg",
        "gambar_tambahan": [
            {
                "gambar": "img/materi/Gambar 2. Gambaran umum sistem reproduksi perempuan..jpeg",
                "keterangan": "Ilustrasi organ reproduksi laki-laki dan perempuan."
            }
        ],
        "isi": [
            {
                "judul": "1. Pengertian Sistem Reproduksi Manusia",
                "paragraf": """
Sistem reproduksi manusia merupakan sekumpulan organ yang bekerja sama
untuk menjalankan proses perkembangbiakan atau menghasilkan keturunan.
Sistem ini merupakan salah satu sistem organ penting dalam tubuh manusia
karena berperan dalam keberlangsungan suatu generasi.

Sistem reproduksi laki-laki dan perempuan memiliki struktur serta fungsi
yang berbeda, tetapi keduanya saling berkaitan dalam proses reproduksi.
Organ reproduksi laki-laki berperan dalam menghasilkan dan menyalurkan
sel sperma, sedangkan organ reproduksi perempuan berperan dalam
menghasilkan sel telur serta mendukung proses perkembangan embrio
dan janin.

Selain berkaitan dengan proses menghasilkan keturunan, sistem reproduksi
juga berhubungan dengan perubahan tubuh selama masa pubertas. Perubahan
tersebut dipengaruhi oleh hormon yang dihasilkan oleh tubuh.
"""
            },
            {
                "judul": "2. Fungsi Sistem Reproduksi",
                "paragraf": """
Sistem reproduksi memiliki beberapa fungsi utama. Fungsi pertama adalah
menghasilkan sel kelamin atau gamet. Pada laki-laki, sel kelamin yang
dihasilkan disebut spermatozoa atau sperma. Sementara itu, pada perempuan
sel kelamin yang dihasilkan disebut ovum atau sel telur.

Fungsi berikutnya adalah mendukung terjadinya proses pembuahan atau
fertilisasi. Fertilisasi merupakan proses penyatuan sel sperma dan sel
telur yang menghasilkan sebuah sel baru bernama zigot. Zigot kemudian
mengalami pembelahan dan perkembangan lebih lanjut.

Pada perempuan, sistem reproduksi juga memiliki fungsi untuk menyediakan
tempat bagi perkembangan embrio dan janin selama kehamilan. Rahim atau
uterus menjadi tempat janin tumbuh hingga siap dilahirkan.
"""
            },
            {
                "judul": "3. Perbedaan Sistem Reproduksi Laki-laki dan Perempuan",
                "paragraf": """
Sistem reproduksi laki-laki memiliki organ utama berupa testis yang
berfungsi menghasilkan sperma dan hormon testosteron. Sperma yang
dihasilkan kemudian mengalami pematangan dan disalurkan melalui
saluran reproduksi.

Sementara itu, sistem reproduksi perempuan memiliki ovarium sebagai
organ yang menghasilkan sel telur. Selain ovarium, terdapat tuba falopi,
rahim, serviks, dan vagina yang memiliki fungsi masing-masing.

Meskipun memiliki struktur yang berbeda, kedua sistem tersebut memiliki
peran yang saling melengkapi dalam proses reproduksi manusia.
"""
            }
        ]
    },


    # ==================================================
    # B. PERTUMBUHAN, PERKEMBANGAN, DAN PUBERTAS
    # ==================================================

    {
        "slug": "pertumbuhan-dan-pubertas",
        "kode": "B",
        "judul": "Pertumbuhan, Perkembangan, dan Pubertas",
        "deskripsi": "Mempelajari perubahan fisik, psikologis, dan perkembangan manusia pada masa pubertas.",
        "gambar": "img/materi/Gambar 3. Ilustrasi perubahan fisik dan pertumbuhan tinggi badan pada masa pubertas..jpeg",
        "gambar_tambahan": [],
        "isi": [
            {
                "judul": "1. Pengertian Pertumbuhan dan Perkembangan",
                "paragraf": """
Pertumbuhan merupakan proses bertambahnya ukuran tubuh, tinggi badan,
berat badan, serta jumlah dan ukuran sel. Pertumbuhan dapat diamati
secara langsung melalui perubahan fisik yang terjadi pada seseorang.

Sementara itu, perkembangan merupakan proses perubahan kemampuan
dan fungsi tubuh menuju tingkat kematangan tertentu. Perkembangan
tidak hanya berkaitan dengan perubahan fisik, tetapi juga mencakup
perkembangan kemampuan berpikir, emosi, dan perilaku.

Pertumbuhan dan perkembangan berlangsung secara bertahap sejak
seseorang dilahirkan hingga mencapai usia dewasa. Setiap individu
dapat mengalami proses pertumbuhan dan perkembangan dengan kecepatan
yang berbeda.
"""
            },
            {
                "judul": "2. Pengertian Pubertas",
                "paragraf": """
Pubertas adalah masa peralihan dari anak-anak menuju dewasa yang
ditandai dengan mulai matangnya organ reproduksi. Pada masa ini,
tubuh mengalami berbagai perubahan akibat meningkatnya aktivitas
hormon tertentu.

Pubertas merupakan proses alami yang dialami oleh setiap manusia.
Waktu dimulainya pubertas tidak selalu sama pada setiap individu.
Ada yang mengalami perubahan lebih awal dan ada pula yang
mengalaminya lebih lambat.

Selama masa pubertas, seseorang mulai mengalami perubahan bentuk
tubuh, pertumbuhan rambut pada bagian tertentu, perubahan suara,
serta perkembangan organ reproduksi.
"""
            },
            {
                "judul": "3. Ciri-ciri Pubertas pada Laki-laki",
                "paragraf": """
Pada laki-laki, pubertas umumnya ditandai dengan perubahan suara
menjadi lebih berat. Hal ini terjadi karena laring atau kotak suara
mengalami perkembangan dan pita suara menjadi lebih panjang.

Selain itu, bahu biasanya menjadi lebih lebar, massa otot meningkat,
dan rambut mulai tumbuh pada ketiak, sekitar kemaluan, serta wajah.
Organ reproduksi juga mengalami perkembangan.

Salah satu tanda penting pubertas pada laki-laki adalah mulai
diproduksinya sel sperma. Pada masa ini, laki-laki juga dapat
mengalami mimpi basah sebagai bagian dari proses pematangan
sistem reproduksi.
"""
            },
            {
                "judul": "4. Ciri-ciri Pubertas pada Perempuan",
                "paragraf": """
Pada perempuan, pubertas umumnya ditandai dengan perkembangan
payudara, pinggul yang mulai melebar, serta tumbuhnya rambut
pada ketiak dan sekitar kemaluan.

Perubahan penting lainnya adalah dimulainya menstruasi atau
haid. Menstruasi merupakan proses keluarnya darah dan jaringan
dari lapisan dinding rahim karena tidak terjadi kehamilan.

Selain perubahan fisik, perempuan juga mengalami perubahan
hormon yang berperan dalam perkembangan organ reproduksi.
Setiap perempuan dapat mengalami waktu pubertas yang berbeda.
"""
            },
            {
                "judul": "5. Cara Menjaga Kesehatan pada Masa Pubertas",
                "paragraf": """
Masa pubertas perlu dihadapi dengan menjaga kesehatan tubuh.
Salah satu caranya adalah menjaga kebersihan diri, terutama
organ reproduksi. Kebersihan perlu dijaga dengan mengganti
pakaian dalam secara teratur dan menggunakan pakaian yang bersih.

Selain itu, penting untuk mengonsumsi makanan bergizi seimbang,
berolahraga secara teratur, tidur yang cukup, dan menjaga
kesehatan mental.

Remaja juga perlu memahami perubahan yang terjadi pada tubuhnya.
Jika mengalami keluhan atau perubahan yang mengkhawatirkan,
sebaiknya berkonsultasi dengan orang tua atau tenaga kesehatan.
"""
            }
        ]
    },


    # ==================================================
    # C. ORGAN REPRODUKSI LAKI-LAKI
    # ==================================================

    {
        "slug": "organ-reproduksi-laki-laki",
        "kode": "C",
        "judul": "Struktur dan Fungsi Organ Reproduksi Laki-laki",
        "deskripsi": "Mengenal bagian-bagian organ reproduksi laki-laki, struktur, dan fungsi setiap organ.",
        "gambar": "img/materi/Gambar 4. Struktur organ reproduksi laki-laki..jpeg",
        "gambar_tambahan": [
            {
                "gambar": "img/materi/Gambar 5. Ilustrasi anatomi sistem reproduksi laki-laki..jpeg",
                "keterangan": "Ilustrasi anatomi sistem reproduksi laki-laki."
            }
        ],
        "isi": [
            {
                "judul": "1. Pengertian Organ Reproduksi Laki-laki",
                "paragraf": """
Organ reproduksi laki-laki merupakan sekumpulan organ yang memiliki
fungsi dalam menghasilkan, menyimpan, dan menyalurkan sel sperma.
Organ-organ tersebut bekerja sama untuk menjalankan proses reproduksi.

Secara umum, organ reproduksi laki-laki dibedakan menjadi organ
reproduksi bagian luar dan bagian dalam. Organ bagian luar meliputi
penis dan skrotum, sedangkan organ bagian dalam meliputi testis,
epididimis, vas deferens, uretra, serta kelenjar reproduksi.

Setiap organ memiliki struktur dan fungsi yang berbeda. Kerja sama
seluruh organ tersebut diperlukan agar proses pembentukan dan
penyaluran sperma dapat berlangsung dengan baik.
"""
            },
            {
                "judul": "2. Testis",
                "paragraf": """
Testis merupakan sepasang organ berbentuk oval yang terletak di
dalam skrotum. Testis memiliki fungsi utama menghasilkan sel sperma
melalui proses yang disebut spermatogenesis.

Selain menghasilkan sperma, testis juga menghasilkan hormon
testosteron. Hormon ini berperan dalam perkembangan ciri-ciri
kelamin sekunder laki-laki, seperti perubahan suara, pertumbuhan
rambut pada wajah, serta perkembangan massa otot.

Di dalam testis terdapat saluran-saluran kecil yang disebut
tubulus seminiferus. Di tempat inilah proses pembentukan
sel sperma berlangsung.
"""
            },
            {
                "judul": "3. Skrotum",
                "paragraf": """
Skrotum merupakan kantong kulit yang berada di bawah penis dan
menjadi tempat bagi testis. Organ ini berfungsi melindungi testis
serta membantu mengatur suhu agar pembentukan sperma dapat
berlangsung secara optimal.

Suhu di dalam skrotum umumnya sedikit lebih rendah dibandingkan
suhu tubuh bagian dalam. Pengaturan suhu tersebut penting karena
proses pembentukan sperma membutuhkan kondisi suhu tertentu.
"""
            },
            {
                "judul": "4. Epididimis",
                "paragraf": """
Epididimis merupakan saluran panjang dan berkelok-kelok yang
terletak di bagian belakang testis. Organ ini menjadi tempat
sperma mengalami proses pematangan setelah dibentuk di dalam testis.

Sperma yang baru dihasilkan belum memiliki kemampuan bergerak
secara optimal. Ketika melewati epididimis, sperma mengalami
proses pematangan sehingga memiliki kemampuan bergerak dan
siap untuk disalurkan melalui saluran reproduksi berikutnya.

Epididimis juga berfungsi sebagai tempat penyimpanan sementara
sel sperma sebelum dikeluarkan melalui proses ejakulasi.
"""
            },
            {
                "judul": "5. Vas Deferens",
                "paragraf": """
Vas deferens merupakan saluran yang menghubungkan epididimis
dengan saluran reproduksi berikutnya. Organ ini memiliki fungsi
mengangkut sperma yang telah matang menuju saluran ejakulasi.

Ketika terjadi ejakulasi, otot-otot pada dinding vas deferens
berkontraksi sehingga membantu mendorong sperma menuju uretra.
Dengan demikian, vas deferens berperan penting dalam proses
penyaluran sel sperma.
"""
            },
            {
                "judul": "6. Uretra dan Penis",
                "paragraf": """
Uretra merupakan saluran yang terdapat di dalam penis dan
berfungsi sebagai saluran keluarnya urine maupun semen dari
tubuh. Meskipun memiliki dua fungsi, urine dan semen tidak
dikeluarkan secara bersamaan.

Penis merupakan organ reproduksi bagian luar yang berfungsi
sebagai alat kopulasi dan menjadi jalan keluarnya semen.
Di dalam penis terdapat jaringan yang dapat terisi darah
sehingga menyebabkan terjadinya ereksi.

Kedua organ ini memiliki peran dalam sistem reproduksi
laki-laki, terutama dalam proses penyaluran semen.
"""
            },
            {
                "judul": "7. Kelenjar Reproduksi",
                "paragraf": """
Selain organ-organ tersebut, sistem reproduksi laki-laki juga
memiliki beberapa kelenjar tambahan. Kelenjar tersebut meliputi
vesikula seminalis, kelenjar prostat, dan kelenjar Cowper.

Vesikula seminalis menghasilkan cairan yang mengandung zat
nutrisi, terutama fruktosa, sebagai sumber energi bagi sperma.
Kelenjar prostat menghasilkan cairan yang menjadi bagian
dari semen dan membantu mendukung fungsi sperma.

Kelenjar Cowper menghasilkan cairan yang membantu melumasi
saluran uretra. Cairan dari berbagai kelenjar tersebut
bercampur dengan sperma membentuk semen.
"""
            }
        ]
    },


    # ==================================================
    # D. ORGAN REPRODUKSI PEREMPUAN
    # ==================================================

    {
        "slug": "organ-reproduksi-perempuan",
        "kode": "D",
        "judul": "Struktur dan Fungsi Organ Reproduksi Perempuan",
        "deskripsi": "Mempelajari bagian-bagian organ reproduksi perempuan dan fungsi masing-masing organ.",
        "gambar": "img/materi/Gambar 7. Struktur organ reproduksi perempuan..jpeg",
        "gambar_tambahan": [
            {
                "gambar": "img/materi/Gambar 6. Ilustrasi organ reproduksi perempuan dan laki-laki..jpeg",
                "keterangan": "Ilustrasi organ reproduksi perempuan dan laki-laki."
            },
            {
                "gambar": "img/materi/Gambar 8. Perbandingan fungsi organ reproduksi laki-laki dan perempuan..jpeg",
                "keterangan": "Perbandingan fungsi organ reproduksi laki-laki dan perempuan."
            }
        ],
        "isi": [
            {
                "judul": "1. Pengertian Organ Reproduksi Perempuan",
                "paragraf": """
Organ reproduksi perempuan merupakan sekumpulan organ yang
berfungsi menghasilkan sel telur, mendukung proses pembuahan,
serta menjadi tempat perkembangan embrio dan janin.

Organ reproduksi perempuan terdiri atas bagian luar dan bagian
dalam. Organ reproduksi bagian dalam meliputi ovarium, tuba
falopi, uterus, serviks, dan vagina. Sementara itu, organ
reproduksi bagian luar secara umum dikenal sebagai vulva.

Setiap organ mempunyai fungsi yang saling berkaitan. Kerja sama
organ-organ tersebut mendukung berlangsungnya siklus menstruasi,
proses fertilisasi, dan kehamilan.
"""
            },
            {
                "judul": "2. Ovarium",
                "paragraf": """
Ovarium atau indung telur merupakan sepasang organ yang
terletak di sebelah kanan dan kiri rahim. Ovarium memiliki
fungsi utama menghasilkan sel telur atau ovum.

Selain menghasilkan sel telur, ovarium juga menghasilkan
hormon estrogen dan progesteron. Kedua hormon tersebut
berperan dalam mengatur siklus menstruasi serta mendukung
perkembangan ciri-ciri kelamin sekunder perempuan.

Pada umumnya, proses pematangan sel telur berlangsung
secara berkala sebagai bagian dari siklus reproduksi.
"""
            },
            {
                "judul": "3. Tuba Falopi",
                "paragraf": """
Tuba falopi atau saluran telur merupakan saluran yang
menghubungkan daerah sekitar ovarium dengan rahim.
Organ ini memiliki fungsi mengangkut sel telur dari
ovarium menuju uterus.

Tuba falopi juga merupakan tempat yang paling umum
terjadinya proses fertilisasi. Ketika sel telur bertemu
dengan sel sperma dan terjadi pembuahan, sel hasil
pembuahan akan bergerak menuju rahim.

Pergerakan tersebut dibantu oleh gerakan silia dan
kontraksi otot pada dinding tuba falopi.
"""
            },
            {
                "judul": "4. Uterus atau Rahim",
                "paragraf": """
Uterus atau rahim merupakan organ berongga yang memiliki
dinding otot cukup tebal. Organ ini menjadi tempat
menempelnya embrio dan berkembangnya janin selama
masa kehamilan.

Dinding bagian dalam rahim disebut endometrium. Lapisan
ini mengalami perubahan selama siklus menstruasi.
Ketika tidak terjadi kehamilan, sebagian lapisan
endometrium akan meluruh dan keluar sebagai darah menstruasi.

Jika terjadi kehamilan, lapisan rahim dipertahankan
untuk mendukung perkembangan awal embrio.
"""
            },
            {
                "judul": "5. Serviks",
                "paragraf": """
Serviks atau leher rahim merupakan bagian bawah uterus
yang menghubungkan rahim dengan vagina. Serviks memiliki
saluran kecil yang memungkinkan darah menstruasi keluar
dari rahim menuju vagina.

Serviks juga berperan dalam proses persalinan. Ketika
persalinan berlangsung, serviks akan mengalami penipisan
dan pembukaan agar bayi dapat melewati jalan lahir.

Selain itu, serviks menghasilkan lendir yang jumlah
dan konsistensinya dapat berubah selama siklus menstruasi.
"""
            },
            {
                "judul": "6. Vagina",
                "paragraf": """
Vagina merupakan saluran berotot dan elastis yang
menghubungkan serviks dengan bagian luar tubuh.
Vagina memiliki beberapa fungsi, antara lain sebagai
saluran keluarnya darah menstruasi, jalan lahir bayi,
serta bagian dari sistem reproduksi perempuan.

Dinding vagina memiliki jaringan yang elastis sehingga
dapat menyesuaikan diri dengan kondisi tubuh. Vagina
juga memiliki mekanisme alami untuk menjaga keseimbangan
lingkungan di dalamnya.

Menjaga kebersihan organ reproduksi bagian luar sangat
penting untuk mendukung kesehatan reproduksi.
"""
            }
        ]
    },


    # ==================================================
    # E. GAMETOGENESIS
    # ==================================================

    {
        "slug": "gametogenesis",
        "kode": "E",
        "judul": "Pembentukan Sel Kelamin (Gametogenesis)",
        "deskripsi": "Memahami proses pembentukan sel sperma dan sel telur pada manusia.",
        "gambar": "img/materi/Gambar 9. Skema proses gametogenesis (oogenesis dan spermatogenesis)..jpeg",
        "gambar_tambahan": [],
        "isi": [
            {
                "judul": "1. Pengertian Gametogenesis",
                "paragraf": """
Gametogenesis merupakan proses pembentukan dan pematangan
sel kelamin atau gamet. Pada manusia, gametogenesis terjadi
di dalam organ reproduksi dan melibatkan pembelahan sel
secara khusus yang disebut meiosis.

Sel kelamin memiliki jumlah kromosom setengah dari jumlah
kromosom sel tubuh manusia. Manusia memiliki 46 kromosom
pada sebagian besar sel tubuhnya, sedangkan sel kelamin
memiliki 23 kromosom.

Ketika sel sperma dan sel telur bersatu dalam proses
fertilisasi, jumlah kromosom kembali menjadi 46.
Dengan demikian, gametogenesis berperan penting dalam
mempertahankan jumlah kromosom manusia dari generasi
ke generasi.
"""
            },
            {
                "judul": "2. Spermatogenesis",
                "paragraf": """
Spermatogenesis merupakan proses pembentukan sel sperma
yang berlangsung di dalam tubulus seminiferus pada testis.
Proses ini mulai berlangsung ketika laki-laki memasuki
masa pubertas.

Spermatogenesis dimulai dari sel induk sperma yang disebut
spermatogonium. Sel tersebut mengalami pembelahan dan
perkembangan hingga terbentuk spermatosit. Selanjutnya,
terjadi pembelahan meiosis yang menghasilkan spermatid.

Spermatid kemudian mengalami perubahan bentuk dan
pematangan sehingga menjadi spermatozoa atau sel sperma
yang memiliki kepala, bagian tengah, dan ekor.

Kepala sperma mengandung materi genetik, bagian tengah
mengandung banyak mitokondria sebagai sumber energi,
sedangkan ekor membantu pergerakan sperma.
"""
            },
            {
                "judul": "3. Oogenesis",
                "paragraf": """
Oogenesis merupakan proses pembentukan sel telur yang
berlangsung di dalam ovarium. Proses ini dimulai sejak
masa perkembangan janin perempuan dan berlanjut kembali
ketika perempuan memasuki masa pubertas.

Dalam proses oogenesis, sel induk telur mengalami
perkembangan melalui beberapa tahap pembelahan.
Hasil akhirnya berupa satu sel telur yang berukuran
besar dan beberapa badan polar yang umumnya mengalami
degenerasi.

Berbeda dengan spermatogenesis yang menghasilkan
beberapa sel sperma dari satu sel induk melalui
pembelahan, oogenesis menghasilkan satu sel telur
fungsional dalam satu rangkaian pembelahan.
"""
            },
            {
                "judul": "4. Perbedaan Spermatogenesis dan Oogenesis",
                "paragraf": """
Spermatogenesis berlangsung di dalam testis, sedangkan
oogenesis berlangsung di dalam ovarium. Spermatogenesis
menghasilkan sel sperma yang berukuran kecil dan dapat
bergerak menggunakan ekor.

Sebaliknya, oogenesis menghasilkan sel telur yang
berukuran lebih besar dan tidak bergerak secara aktif.
Sel telur memiliki cadangan sitoplasma yang mendukung
tahap awal perkembangan setelah fertilisasi.

Kedua proses tersebut sama-sama penting karena
menghasilkan sel kelamin yang dibutuhkan dalam
proses reproduksi manusia.
"""
            }
        ]
    },


    # ==================================================
    # F. SIKLUS MENSTRUASI
    # ==================================================

    {
        "slug": "siklus-menstruasi",
        "kode": "F",
        "judul": "Siklus Menstruasi",
        "deskripsi": "Memahami tahapan menstruasi dan perubahan hormon dalam sistem reproduksi perempuan.",
        "gambar": "img/materi/Gambar 10. Grafik perubahan kadar hormon dan siklus menstruasi..jpeg",
        "gambar_tambahan": [
            {
                "gambar": "img/materi/Gambar 11. Tahapan proses ovulasi dan pengaturan hormon reproduksi..jpeg",
                "keterangan": "Tahapan proses ovulasi dan pengaturan hormon reproduksi."
            }
        ],
        "isi": [
            {
                "judul": "1. Pengertian Siklus Menstruasi",
                "paragraf": """
Siklus menstruasi merupakan rangkaian perubahan berkala
yang terjadi pada sistem reproduksi perempuan. Perubahan
ini melibatkan ovarium dan lapisan dinding rahim atau
endometrium.

Siklus menstruasi dihitung sejak hari pertama menstruasi
hingga satu hari sebelum menstruasi berikutnya dimulai.
Panjang siklus berbeda-beda pada setiap perempuan.
Siklus 28 hari sering digunakan sebagai contoh untuk
menjelaskan tahapan menstruasi, tetapi siklus normal
dapat memiliki variasi.

Perubahan selama siklus menstruasi dipengaruhi oleh
hormon estrogen, progesteron, FSH, dan LH.
"""
            },
            {
                "judul": "2. Fase Menstruasi",
                "paragraf": """
Fase menstruasi merupakan tahap ketika lapisan
endometrium yang sebelumnya menebal mengalami peluruhan.
Peluruhan tersebut menyebabkan darah dan jaringan
keluar melalui vagina.

Fase ini terjadi ketika tidak terdapat kehamilan.
Penurunan kadar hormon estrogen dan progesteron
menjadi salah satu faktor yang memicu peluruhan
lapisan dinding rahim.

Lama menstruasi dapat berbeda pada setiap perempuan.
Selama fase ini, sebagian perempuan dapat mengalami
kram perut, perubahan suasana hati, atau rasa lelah.
"""
            },
            {
                "judul": "3. Fase Folikular",
                "paragraf": """
Fase folikular dimulai pada hari pertama menstruasi
dan berlangsung hingga menjelang ovulasi. Pada tahap
ini, hormon FSH membantu merangsang pertumbuhan
beberapa folikel di dalam ovarium.

Folikel merupakan struktur yang berisi sel telur
yang sedang mengalami pematangan. Salah satu folikel
biasanya berkembang lebih dominan dibandingkan
folikel lainnya.

Folikel yang berkembang menghasilkan hormon estrogen.
Hormon tersebut membantu merangsang penebalan kembali
lapisan endometrium sebagai persiapan jika terjadi
kehamilan.
"""
            },
            {
                "judul": "4. Fase Ovulasi",
                "paragraf": """
Ovulasi merupakan proses pelepasan sel telur yang
telah matang dari ovarium. Proses ini dipicu oleh
peningkatan hormon LH atau luteinizing hormone.

Setelah dilepaskan, sel telur bergerak menuju
tuba falopi. Pada tahap ini, sel telur memiliki
kemungkinan untuk bertemu dengan sel sperma.

Waktu ovulasi tidak selalu sama pada setiap perempuan.
Pada siklus 28 hari, ovulasi sering diperkirakan
terjadi sekitar pertengahan siklus, tetapi waktu
sebenarnya dapat berbeda.
"""
            },
            {
                "judul": "5. Fase Luteal",
                "paragraf": """
Setelah ovulasi, sisa folikel yang telah melepaskan
sel telur berubah menjadi struktur yang disebut
korpus luteum.

Korpus luteum menghasilkan hormon progesteron
dan sejumlah estrogen. Progesteron berfungsi
membantu mempertahankan ketebalan endometrium
agar siap mendukung kemungkinan terjadinya
kehamilan.

Apabila tidak terjadi kehamilan, korpus luteum
akan mengalami penyusutan. Kadar progesteron
dan estrogen menurun sehingga lapisan endometrium
kembali meluruh dan siklus menstruasi berikutnya
dimulai.
"""
            }
        ]
    },


    # ==================================================
    # G. FERTILISASI DAN PROSES KEHAMILAN
    # ==================================================

    {
        "slug": "fertilisasi-dan-kehamilan",
        "kode": "G",
        "judul": "Fertilisasi dan Proses Kehamilan",
        "deskripsi": "Mempelajari proses pertemuan sel sperma dan sel telur hingga terbentuknya embrio.",
        "gambar": "img/materi/Gambar 12. Proses penetrasi sperma dan fertilisasi sel telur..jpeg",
        "gambar_tambahan": [
            {
                "gambar": "img/materi/Gambar 13. Tahapan perkembangan awal embrio manusia (Carnegie Stages)..jpeg",
                "keterangan": "Tahapan perkembangan awal embrio manusia (Carnegie Stages)."
            }
        ],
        "isi": [
            {
                "judul": "1. Pengertian Fertilisasi",
                "paragraf": """
Fertilisasi atau pembuahan merupakan proses penyatuan
sel sperma dengan sel telur. Pada manusia, proses
ini umumnya berlangsung di bagian tuba falopi.

Sel sperma membawa materi genetik dari ayah, sedangkan
sel telur membawa materi genetik dari ibu. Ketika
keduanya berhasil bersatu, terbentuklah satu sel
baru yang disebut zigot.

Zigot memiliki jumlah kromosom sebanyak 46, yaitu
gabungan 23 kromosom dari sel sperma dan 23 kromosom
dari sel telur.
"""
            },
            {
                "judul": "2. Tahapan Terjadinya Fertilisasi",
                "paragraf": """
Proses fertilisasi dimulai ketika sel sperma bergerak
menuju saluran reproduksi perempuan setelah dikeluarkan
melalui proses ejakulasi. Dari jutaan sel sperma,
hanya sebagian kecil yang berhasil mencapai daerah
sekitar sel telur.

Sel sperma yang berhasil mendekati sel telur akan
berinteraksi dengan lapisan pelindung sel telur.
Setelah satu sel sperma berhasil masuk, mekanisme
tertentu akan membantu mencegah masuknya sel sperma
lain.

Inti sel sperma kemudian bersatu dengan inti sel telur
sehingga terbentuk zigot. Zigot menjadi awal dari
perkembangan individu baru.
"""
            },
            {
                "judul": "3. Perkembangan Zigot Menjadi Embrio",
                "paragraf": """
Setelah fertilisasi, zigot mengalami pembelahan
sel berulang kali. Pembelahan tersebut menghasilkan
kumpulan sel yang semakin banyak tanpa langsung
menambah ukuran keseluruhan struktur.

Zigot kemudian berkembang melalui beberapa tahap,
antara lain morula dan blastokista. Blastokista
selanjutnya bergerak menuju rahim.

Setelah mencapai rahim, blastokista dapat menempel
pada lapisan endometrium melalui proses yang disebut
implantasi. Implantasi merupakan salah satu tahap
penting dalam awal kehamilan.
"""
            },
            {
                "judul": "4. Pengertian Implantasi",
                "paragraf": """
Implantasi merupakan proses menempelnya blastokista
pada dinding rahim. Proses ini memungkinkan embrio
memperoleh dukungan lingkungan dan nutrisi dari
tubuh ibu untuk melanjutkan perkembangannya.

Setelah implantasi berlangsung, jaringan yang
berkaitan dengan pembentukan plasenta mulai
berkembang. Plasenta nantinya berperan dalam
pertukaran oksigen, zat makanan, dan sisa
metabolisme antara ibu dan janin.
"""
            }
        ]
    },


    # ==================================================
    # H. KEHAMILAN DAN PERKEMBANGAN JANIN
    # ==================================================

    {
        "slug": "perkembangan-janin",
        "kode": "H",
        "judul": "Kehamilan dan Perkembangan Janin",
        "deskripsi": "Mengenal perkembangan embrio dan janin serta peran organ pendukung selama kehamilan.",
        "gambar": "img/materi/Gambar 14. Proses terjadinya kehamilan dan tahap perkembangan janin..jpeg",
        "gambar_tambahan": [],
        "isi": [
            {
                "judul": "1. Pengertian Kehamilan",
                "paragraf": """
Kehamilan merupakan kondisi ketika embrio berkembang
di dalam rahim setelah proses fertilisasi dan
implantasi berhasil berlangsung.

Selama kehamilan, tubuh ibu mengalami berbagai
perubahan untuk mendukung pertumbuhan dan perkembangan
janin. Perubahan tersebut melibatkan hormon,
sistem peredaran darah, serta organ-organ tubuh lainnya.

Masa kehamilan manusia umumnya berlangsung sekitar
40 minggu jika dihitung dari hari pertama menstruasi
terakhir. Selama periode tersebut, perkembangan
janin berlangsung secara bertahap.
"""
            },
            {
                "judul": "2. Perkembangan Embrio dan Janin",
                "paragraf": """
Pada tahap awal, hasil pembuahan berkembang menjadi
embrio. Sel-sel embrio mengalami pembelahan dan
diferensiasi, yaitu proses ketika sel mulai memiliki
struktur serta fungsi yang berbeda.

Selanjutnya, berbagai organ tubuh mulai terbentuk
dan berkembang. Proses pembentukan organ ini
dikenal sebagai organogenesis.

Setelah memasuki tahap perkembangan berikutnya,
embrio disebut janin. Pada tahap ini, organ-organ
yang telah terbentuk terus mengalami pertumbuhan
dan pematangan hingga mendekati waktu kelahiran.
"""
            },
            {
                "judul": "3. Fungsi Plasenta",
                "paragraf": """
Plasenta merupakan organ sementara yang terbentuk
selama kehamilan dan menghubungkan kebutuhan
perkembangan janin dengan tubuh ibu.

Salah satu fungsi utama plasenta adalah membantu
pertukaran oksigen dan zat makanan dari darah ibu
ke darah janin. Plasenta juga membantu membawa
sisa metabolisme dari janin menuju tubuh ibu
untuk dikeluarkan.

Selain itu, plasenta menghasilkan hormon yang
membantu mempertahankan kehamilan dan mendukung
perubahan tubuh ibu selama masa kehamilan.
"""
            },
            {
                "judul": "4. Fungsi Tali Pusat dan Air Ketuban",
                "paragraf": """
Tali pusat merupakan penghubung antara janin
dengan plasenta. Di dalam tali pusat terdapat
pembuluh darah yang berfungsi mengangkut oksigen,
zat makanan, dan sisa metabolisme.

Sementara itu, air ketuban merupakan cairan
yang mengelilingi janin di dalam kantung ketuban.
Cairan ini berfungsi melindungi janin dari
benturan, membantu menjaga suhu, dan memberikan
ruang bagi janin untuk bergerak.

Plasenta, tali pusat, dan air ketuban memiliki
peran penting dalam mendukung perkembangan
janin selama berada di dalam rahim.
"""
            }
        ]
    },


    # ==================================================
    # I. PROSES KELAHIRAN MANUSIA
    # ==================================================

    {
        "slug": "proses-kelahiran",
        "kode": "I",
        "judul": "Proses Kelahiran Manusia",
        "deskripsi": "Mempelajari tahapan persalinan dan proses keluarnya bayi dari rahim ibu.",
        "gambar": "img/materi/Gambar 14. Proses terjadinya kehamilan dan tahap perkembangan janin..jpeg",
        "gambar_tambahan": [],
        "isi": [
            {
                "judul": "1. Pengertian Kelahiran",
                "paragraf": """
Kelahiran atau persalinan merupakan proses keluarnya
bayi dari rahim ibu setelah mengalami perkembangan
selama masa kehamilan.

Proses persalinan melibatkan kerja sama berbagai
organ dan hormon. Menjelang persalinan, otot rahim
mengalami kontraksi yang membantu mendorong bayi
menuju jalan lahir.

Persalinan dapat berlangsung melalui persalinan
pervaginam atau melalui tindakan operasi sesar,
bergantung pada kondisi ibu dan bayi serta
pertimbangan tenaga kesehatan.
"""
            },
            {
                "judul": "2. Tahap Pertama: Pembukaan Serviks",
                "paragraf": """
Tahap pertama persalinan ditandai dengan kontraksi
rahim yang membantu serviks mengalami penipisan
dan pembukaan.

Pembukaan serviks diperlukan agar bayi dapat
melewati jalan lahir. Kontraksi dapat berlangsung
secara bertahap dengan intensitas dan frekuensi
yang semakin meningkat.

Lama tahap ini berbeda-beda pada setiap ibu.
Kondisi kesehatan ibu, pengalaman persalinan,
dan faktor lainnya dapat memengaruhi proses tersebut.
"""
            },
            {
                "judul": "3. Tahap Kedua: Pengeluaran Bayi",
                "paragraf": """
Tahap kedua berlangsung ketika serviks telah
membuka lengkap dan bayi mulai bergerak melewati
jalan lahir.

Kontraksi rahim bersama dorongan ibu membantu
bayi bergerak keluar melalui vagina. Setelah
bayi lahir, tenaga kesehatan akan melakukan
pemeriksaan awal untuk memastikan kondisi bayi.

Pada kondisi tertentu, tenaga kesehatan dapat
membantu proses kelahiran menggunakan tindakan
medis sesuai kebutuhan.
"""
            },
            {
                "judul": "4. Tahap Ketiga: Pengeluaran Plasenta",
                "paragraf": """
Setelah bayi dilahirkan, proses persalinan
berlanjut pada pengeluaran plasenta atau ari-ari.
Plasenta yang sebelumnya berfungsi mendukung
perkembangan janin akan terlepas dari dinding rahim.

Rahim kemudian terus berkontraksi untuk membantu
mengeluarkan plasenta dan mengurangi perdarahan.
Tenaga kesehatan akan memastikan plasenta
keluar dengan lengkap.

Setelah persalinan, ibu dan bayi tetap memerlukan
pemantauan kesehatan serta perawatan yang sesuai.
"""
            }
        ]
    },


    # ==================================================
    # J. KELUARGA BERENCANA
    # ==================================================

    {
        "slug": "keluarga-berencana",
        "kode": "J",
        "judul": "Keluarga Berencana dan Pengaturan Reproduksi",
        "deskripsi": "Mengenal tujuan keluarga berencana, perencanaan kehamilan, dan kesehatan reproduksi.",
        "gambar": "img/materi/Gambar 15. Simbol program Keluarga Berencana (KB)..jpeg",
        "gambar_tambahan": [],
        "isi": [
            {
                "judul": "1. Pengertian Keluarga Berencana",
                "paragraf": """
Keluarga Berencana atau KB merupakan upaya yang dilakukan
untuk membantu pasangan merencanakan kehamilan,
mengatur jarak kelahiran, dan menentukan jumlah anak
sesuai dengan kondisi keluarga.

Keluarga berencana tidak hanya berkaitan dengan
pengaturan kehamilan, tetapi juga berhubungan
dengan kesehatan ibu, anak, dan kesejahteraan keluarga.

Perencanaan reproduksi yang baik dapat membantu
keluarga mempersiapkan kebutuhan kesehatan,
pendidikan, serta kebutuhan ekonomi.
"""
            },
            {
                "judul": "2. Tujuan Keluarga Berencana",
                "paragraf": """
Salah satu tujuan keluarga berencana adalah membantu
mengatur jarak kelahiran agar kesehatan ibu dan anak
dapat lebih diperhatikan.

Selain itu, keluarga berencana bertujuan membantu
pasangan merencanakan kehamilan berdasarkan kesiapan
fisik, mental, dan kondisi keluarga.

Program keluarga berencana juga mendukung upaya
peningkatan kesehatan reproduksi melalui pemberian
informasi dan pelayanan kesehatan yang tepat.
"""
            },
            {
                "judul": "3. Metode Kontrasepsi",
                "paragraf": """
Kontrasepsi merupakan metode atau alat yang digunakan
untuk mencegah atau menunda kehamilan. Terdapat
berbagai jenis kontrasepsi dengan cara kerja
dan tingkat efektivitas yang berbeda.

Contohnya adalah kondom, pil kontrasepsi,
suntik kontrasepsi, implan, alat kontrasepsi
dalam rahim, dan metode kontrasepsi lainnya.

Pemilihan metode kontrasepsi perlu mempertimbangkan
kondisi kesehatan, kebutuhan, dan konsultasi
dengan tenaga kesehatan.
"""
            },
            {
                "judul": "4. Pentingnya Perencanaan Reproduksi",
                "paragraf": """
Perencanaan reproduksi membantu seseorang dan
keluarga memahami tanggung jawab yang berkaitan
dengan kesehatan reproduksi.

Pengetahuan mengenai kesehatan reproduksi juga
membantu masyarakat memahami pentingnya pemeriksaan
kesehatan, menjaga kebersihan diri, serta mencari
informasi dari sumber yang dapat dipercaya.

Dengan pemahaman yang baik, keputusan yang
berkaitan dengan kesehatan reproduksi dapat
dilakukan secara lebih bertanggung jawab.
"""
            }
        ]
    },


    # ==================================================
    # K. GANGGUAN DAN PENYAKIT SISTEM REPRODUKSI
    # ==================================================

    {
        "slug": "gangguan-penyakit-reproduksi",
        "kode": "K",
        "judul": "Gangguan dan Penyakit pada Sistem Reproduksi Manusia",
        "deskripsi": "Mengenal beberapa gangguan sistem reproduksi serta cara menjaga kesehatan reproduksi.",
        "gambar": "img/materi/Gambar 16. Infografis gangguan endometriosis pada sistem reproduksi perempuan..jpeg",
        "gambar_tambahan": [],
        "isi": [
            {
                "judul": "1. Pengertian Gangguan Sistem Reproduksi",
                "paragraf": """
Sistem reproduksi dapat mengalami gangguan yang
memengaruhi fungsi organ maupun kesehatan seseorang.
Gangguan tersebut dapat disebabkan oleh infeksi,
perubahan hormon, kelainan struktur organ,
atau faktor kesehatan lainnya.

Gangguan sistem reproduksi dapat dialami oleh
laki-laki maupun perempuan. Gejala yang muncul
juga berbeda-beda, bergantung pada jenis gangguan
dan kondisi setiap individu.

Memahami gangguan sistem reproduksi penting
agar seseorang dapat mengenali gejala awal
dan memperoleh pemeriksaan kesehatan yang tepat.
"""
            },
            {
                "judul": "2. Infeksi pada Sistem Reproduksi",
                "paragraf": """
Infeksi pada sistem reproduksi dapat disebabkan
oleh mikroorganisme seperti bakteri, virus,
atau jamur. Beberapa infeksi dapat menimbulkan
gejala berupa nyeri, gatal, perubahan cairan,
luka, atau rasa tidak nyaman pada organ reproduksi.

Sebagian infeksi dapat ditularkan melalui
kontak seksual, sedangkan infeksi lainnya
dapat berkaitan dengan faktor kebersihan
atau kondisi kesehatan tertentu.

Pemeriksaan oleh tenaga kesehatan diperlukan
untuk mengetahui penyebab gangguan dan
menentukan penanganan yang sesuai.
"""
            },
            {
                "judul": "3. Contoh Gangguan Sistem Reproduksi",
                "paragraf": """
Beberapa contoh gangguan pada sistem reproduksi
perempuan adalah endometriosis, kista ovarium,
dan gangguan siklus menstruasi. Endometriosis
merupakan kondisi ketika jaringan yang mirip
dengan lapisan rahim tumbuh di luar rahim.

Pada laki-laki, salah satu gangguan yang dapat
terjadi adalah varikokel, yaitu pelebaran
pembuluh darah vena pada skrotum. Gangguan
lainnya dapat berkaitan dengan peradangan
atau infeksi pada organ reproduksi.

Tidak semua gangguan menunjukkan gejala yang
sama. Oleh karena itu, pemeriksaan medis
diperlukan untuk memastikan diagnosis.
"""
            },
            {
                "judul": "4. Cara Menjaga Kesehatan Reproduksi",
                "paragraf": """
Kesehatan reproduksi dapat dijaga dengan
menerapkan kebiasaan hidup bersih dan sehat.
Salah satu langkah penting adalah menjaga
kebersihan organ reproduksi dan mengganti
pakaian dalam secara teratur.

Selain itu, penting untuk menggunakan
pakaian yang bersih, mengonsumsi makanan
bergizi, berolahraga, dan mendapatkan
istirahat yang cukup.

Seseorang juga perlu menghindari perilaku
berisiko serta tidak menggunakan barang
pribadi secara bergantian apabila berpotensi
menularkan infeksi.

Jika mengalami gejala seperti nyeri,
perdarahan yang tidak biasa, luka,
atau perubahan cairan yang tidak normal,
sebaiknya segera berkonsultasi dengan
tenaga kesehatan.
"""
            }
        ]
    },


    # ==================================================
    # L. RANGKUMAN MATERI
    # ==================================================

    {
        "slug": "rangkuman",
        "kode": "L",
        "judul": "Rangkuman Materi",
        "deskripsi": "Mengulas kembali konsep penting tentang sistem reproduksi manusia dari awal hingga akhir.",
        "gambar": "img/materi/Gambar 8. Perbandingan fungsi organ reproduksi laki-laki dan perempuan..jpeg",
        "gambar_tambahan": [],
        "isi": [
            {
                "judul": "1. Sistem Reproduksi Manusia",
                "paragraf": """
Sistem reproduksi manusia merupakan sistem organ
yang berfungsi dalam proses menghasilkan keturunan.
Sistem ini terdiri atas organ reproduksi laki-laki
dan perempuan yang memiliki struktur serta fungsi
masing-masing.

Organ reproduksi laki-laki berperan dalam
menghasilkan dan menyalurkan sperma, sedangkan
organ reproduksi perempuan berperan menghasilkan
sel telur dan mendukung perkembangan embrio
serta janin.
"""
            },
            {
                "judul": "2. Pertumbuhan dan Pubertas",
                "paragraf": """
Pubertas merupakan masa peralihan dari anak-anak
menuju dewasa yang ditandai dengan perubahan fisik,
hormonal, dan perkembangan organ reproduksi.

Pada laki-laki, perubahan dapat berupa suara
yang menjadi lebih berat, pertumbuhan rambut,
dan mulai diproduksinya sperma. Pada perempuan,
perubahan dapat berupa perkembangan payudara,
perubahan bentuk tubuh, dan dimulainya menstruasi.
"""
            },
            {
                "judul": "3. Organ Reproduksi Laki-laki dan Perempuan",
                "paragraf": """
Organ reproduksi laki-laki meliputi testis,
skrotum, epididimis, vas deferens, uretra,
penis, serta kelenjar reproduksi.

Organ reproduksi perempuan meliputi ovarium,
tuba falopi, uterus, serviks, vagina, dan
organ reproduksi bagian luar.

Masing-masing organ memiliki fungsi yang
saling mendukung dalam proses reproduksi.
"""
            },
            {
                "judul": "4. Pembentukan Sel Kelamin",
                "paragraf": """
Pembentukan sel kelamin disebut gametogenesis.
Pada laki-laki, proses pembentukan sperma
disebut spermatogenesis dan berlangsung
di dalam testis.

Pada perempuan, pembentukan sel telur
disebut oogenesis dan berlangsung
di dalam ovarium.

Kedua proses tersebut menghasilkan
sel kelamin yang memiliki 23 kromosom.
"""
            },
            {
                "judul": "5. Menstruasi, Fertilisasi, dan Kehamilan",
                "paragraf": """
Siklus menstruasi merupakan rangkaian perubahan
pada sistem reproduksi perempuan yang melibatkan
perubahan hormon dan lapisan dinding rahim.

Apabila sel sperma bertemu dan bersatu dengan
sel telur, dapat terjadi fertilisasi yang
menghasilkan zigot. Zigot berkembang melalui
beberapa tahap hingga menjadi embrio dan
mengalami implantasi pada dinding rahim.

Selama kehamilan, embrio dan janin berkembang
di dalam rahim dengan dukungan plasenta,
tali pusat, dan air ketuban.
"""
            },
            {
                "judul": "6. Kelahiran dan Kesehatan Reproduksi",
                "paragraf": """
Kelahiran merupakan proses keluarnya bayi
dari rahim setelah masa kehamilan.
Persalinan secara umum meliputi pembukaan
serviks, pengeluaran bayi, dan pengeluaran
plasenta.

Kesehatan reproduksi perlu dijaga dengan
menerapkan kebersihan diri, pola hidup sehat,
serta memahami perubahan yang terjadi
pada tubuh.

Pengetahuan tentang sistem reproduksi
membantu setiap orang memahami fungsi
organ tubuh dan menjaga kesehatan
reproduksi secara bertanggung jawab.
"""
            }
        ]
    },
]


# ==================================================
# DATA KUIS
# ==================================================

SOAL_KUIS = [
    {
        "soal": "Apa fungsi utama sistem reproduksi manusia?",
        "pilihan": [
            "Menghasilkan energi",
            "Menghasilkan keturunan",
            "Mengatur pernapasan",
            "Mengolah makanan"
        ],
        "jawaban": 1,
        "pembahasan": "Sistem reproduksi bekerja sama menjalankan fungsi reproduksi atau menghasilkan keturunan."
    },
    {
        "soal": "Sel kelamin jantan (sperma) dan sel kelamin betina (ovum) masing-masing membawa berapa kromosom pada manusia?",
        "pilihan": [
            "46 kromosom",
            "44 kromosom",
            "23 kromosom",
            "22 kromosom"
        ],
        "jawaban": 2,
        "pembahasan": "Sel tubuh manusia umumnya memiliki 46 kromosom, sedangkan sel kelamin matang membawa setengahnya yaitu 23 kromosom."
    },
    {
        "soal": "Perbedaan utama antara pertumbuhan dan perkembangan adalah ...",
        "pilihan": [
            "Pertumbuhan bersifat kualitatif, perkembangan bersifat kuantitatif",
            "Pertumbuhan bersifat kuantitatif (terukur), perkembangan bersifat kualitatif menuju kematangan fungsi",
            "Pertumbuhan hanya terjadi saat pubertas, perkembangan terjadi seumur hidup",
            "Pertumbuhan tidak melibatkan perubahan ukuran tubuh"
        ],
        "jawaban": 1,
        "pembahasan": "Pertumbuhan bersifat kuantitatif (bertambahnya ukuran, massa, tinggi badan), sedangkan perkembangan bersifat kualitatif (perubahan struktur dan fungsi menuju kematangan)."
    },
    {
        "soal": "Masa peralihan dari anak-anak menuju dewasa yang ditandai kematangan organ reproduksi dan ciri seksual sekunder disebut ...",
        "pilihan": [
            "Fertilisasi",
            "Implantasi",
            "Pubertas",
            "Organogenesis"
        ],
        "jawaban": 2,
        "pembahasan": "Pubertas adalah masa peralihan dari anak-anak menuju dewasa akibat perubahan aktivitas hormon."
    },
    {
        "soal": "Ciri pubertas yang umumnya terjadi pada laki-laki adalah ...",
        "pilihan": [
            "Pinggul melebar dan payudara berkembang",
            "Suara menjadi lebih berat, massa otot meningkat, dan produksi sperma dimulai",
            "Dimulainya siklus menstruasi bulanan",
            "Berkurangnya pertumbuhan rambut pada tubuh"
        ],
        "jawaban": 1,
        "pembahasan": "Pada laki-laki, pubertas ditandai dengan pematangan organ reproduksi, produksi sperma, suara memberat, pertumbuhan rambut, dan peningkatan massa otot."
    },
    {
        "soal": "Hormon yang dihasilkan hipotalamus dan mengatur pelepasan FSH serta LH dari kelenjar hipofisis adalah ...",
        "pilihan": [
            "GnRH",
            "Testosteron",
            "Progesteron",
            "Oksitosin"
        ],
        "jawaban": 0,
        "pembahasan": "GnRH dihasilkan oleh hipotalamus untuk mengatur pelepasan FSH dan LH oleh kelenjar hipofisis."
    },
    {
        "soal": "Organ reproduksi bagian luar laki-laki yang berfungsi membungkus testis dan mengatur suhunya adalah ...",
        "pilihan": [
            "Epididimis",
            "Vesikula seminalis",
            "Skrotum",
            "Kelenjar prostat"
        ],
        "jawaban": 2,
        "pembahasan": "Skrotum adalah kantong kulit yang membungkus dan melindungi testis serta membantu mengatur suhu agar sesuai untuk pembentukan sperma."
    },
    {
        "soal": "Bagian di dalam testis yang menjadi tempat berlangsungnya pembentukan sel sperma adalah ...",
        "pilihan": [
            "Tubulus seminiferus",
            "Vas deferens",
            "Kelenjar Cowper",
            "Saluran ejakulasi"
        ],
        "jawaban": 0,
        "pembahasan": "Sperma dibentuk di dalam tubulus seminiferus yang terdapat di dalam testis."
    },
    {
        "soal": "Saluran panjang berkelok-kelok di bagian belakang testis yang berfungsi sebagai tempat pematangan dan penyimpanan sementara sperma adalah ...",
        "pilihan": [
            "Uretra",
            "Epididimis",
            "Vesikula seminalis",
            "Penis"
        ],
        "jawaban": 1,
        "pembahasan": "Epididimis merupakan saluran berkelok-kelok di bagian belakang testis tempat pematangan dan penyimpanan sementara sperma."
    },
    {
        "soal": "Kelenjar reproduksi laki-laki yang menghasilkan cairan kaya fruktosa sebagai sumber energi bagi sperma adalah ...",
        "pilihan": [
            "Vesikula seminalis",
            "Kelenjar bulbouretra (Cowper)",
            "Skrotum",
            "Endometrium"
        ],
        "jawaban": 0,
        "pembahasan": "Vesikula seminalis menghasilkan cairan kaya fruktosa sebagai sumber energi bagi sperma dan menjadi salah satu komponen semen."
    },
    {
        "soal": "Urutan jalur perjalanan sperma yang tepat dari tempat pembentukan hingga keluar tubuh adalah ...",
        "pilihan": [
            "Testis → vas deferens → epididimis → uretra → saluran ejakulasi",
            "Testis → epididimis → vas deferens → saluran ejakulasi → uretra",
            "Epididimis → testis → saluran ejakulasi → vas deferens → uretra",
            "Vas deferens → testis → epididimis → uretra → saluran ejakulasi"
        ],
        "jawaban": 1,
        "pembahasan": "Urutan jalur sperma adalah testis → epididimis → vas deferens → saluran ejakulasi → uretra."
    },
    {
        "soal": "Istilah keseluruhan bagian luar organ genital perempuan disebut ...",
        "pilihan": [
            "Serviks",
            "Endometrium",
            "Vulva",
            "Oviduk"
        ],
        "jawaban": 2,
        "pembahasan": "Vulva merupakan istilah untuk keseluruhan bagian luar organ genital perempuan, yang meliputi labia mayora dan labia minora."
    },
    {
        "soal": "Saluran yang menghubungkan daerah sekitar ovarium dengan rahim serta menjadi lokasi umum terjadinya fertilisasi adalah ...",
        "pilihan": [
            "Tuba falopi (oviduk)",
            "Serviks",
            "Vagina",
            "Kelenjar prostat"
        ],
        "jawaban": 0,
        "pembahasan": "Tuba falopi (oviduk) mengangkut sel telur dari ovarium menuju rahim dan menjadi lokasi umum terjadinya fertilisasi."
    },
    {
        "soal": "Lapisan dinding rahim (uterus) yang menebal untuk persiapan implantasi embrio atau meluruh saat menstruasi disebut ...",
        "pilihan": [
            "Perimetrium",
            "Miometrium",
            "Endometrium",
            "Amnion"
        ],
        "jawaban": 2,
        "pembahasan": "Endometrium adalah lapisan dalam dinding rahim yang menebal untuk persiapan implantasi atau meluruh saat menstruasi."
    },
    {
        "soal": "Proses pembentukan dan pematangan sel kelamin (gamet) melalui pembelahan meiosis disebut ...",
        "pilihan": [
            "Mitosis",
            "Gametogenesis",
            "Ovulasi",
            "Implantasi"
        ],
        "jawaban": 1,
        "pembahasan": "Gametogenesis adalah proses pembentukan sel kelamin melalui pembelahan meiosis sehingga menghasilkan sel dengan setengah jumlah kromosom."
    },
    {
        "soal": "Berapa jumlah sel fungsional yang umumnya dihasilkan dari satu oosit primer pada proses oogenesis?",
        "pilihan": [
            "Empat sel telur fungsional",
            "Dua sel telur fungsional",
            "Satu sel telur fungsional",
            "Delapan sel telur fungsional"
        ],
        "jawaban": 2,
        "pembahasan": "Berbeda dengan spermatogenesis yang menghasilkan empat sel sperma fungsional, oogenesis umumnya menghasilkan satu sel telur fungsional."
    },
    {
        "soal": "Fase dalam siklus menstruasi yang ditandai pelepasan oosit sekunder dari ovarium dan umumnya dipicu lonjakan hormon LH adalah ...",
        "pilihan": [
            "Fase menstruasi",
            "Fase ovulasi",
            "Fase luteal",
            "Fase implantasi"
        ],
        "jawaban": 1,
        "pembahasan": "Fase ovulasi adalah pelepasan oosit sekunder dari ovarium yang umumnya dipicu oleh peningkatan tajam hormon LH."
    },
    {
        "soal": "Setelah ovulasi, sisa folikel berubah menjadi korpus luteum yang menghasilkan hormon apa untuk mempertahankan endometrium?",
        "pilihan": [
            "Progesteron dan sejumlah estrogen",
            "Oksitosin dan prostaglandin",
            "Testosteron dan GnRH",
            "Adrenalin dan insulin"
        ],
        "jawaban": 0,
        "pembahasan": "Korpus luteum menghasilkan progesteron dan sejumlah estrogen yang membantu mempertahankan kondisi dinding endometrium."
    },
    {
        "soal": "Tahapan perkembangan awal setelah fertilisasi yang berbentuk kumpulan sel padat menyerupai bola sebelum blastokista adalah ...",
        "pilihan": [
            "Zigot",
            "Morula",
            "Janin",
            "Plasenta"
        ],
        "jawaban": 1,
        "pembahasan": "Setelah zigot membelah, terbentuk morula (bola sel padat), kemudian blastokista, lalu menempel pada endometrium (implantasi)."
    },
    {
        "soal": "Usia kehamilan secara medis umumnya dihitung sekitar berapa minggu sejak hari pertama menstruasi terakhir?",
        "pilihan": [
            "20 minggu",
            "28 minggu",
            "40 minggu",
            "52 minggu"
        ],
        "jawaban": 2,
        "pembahasan": "Usia kehamilan secara medis umumnya dihitung sekitar 40 minggu sejak hari pertama menstruasi terakhir."
    },
    {
        "soal": "Struktur pendukung kehamilan yang menjadi tempat pertukaran oksigen, zat gizi, dan sisa metabolisme antara darah ibu dan janin adalah ...",
        "pilihan": [
            "Plasenta",
            "Serviks",
            "Tuba falopi",
            "Epididimis"
        ],
        "jawaban": 0,
        "pembahasan": "Plasenta merupakan organ sementara tempat pertukaran oksigen, zat gizi, dan sisa metabolisme antara ibu dan janin."
    },
    {
        "soal": "Kembar identik (monozigotik) terjadi apabila ...",
        "pilihan": [
            "Dua sel telur dibuahi oleh dua sel sperma berbeda",
            "Satu zigot membelah menjadi dua embrio dengan materi genetik sangat mirip",
            "Satu sel telur dibuahi dua sperma pada waktu berbeda",
            "Dua ovum matang dari ovarium yang sama tanpa pembuahan"
        ],
        "jawaban": 1,
        "pembahasan": "Kembar identik (monozigotik) terjadi ketika satu zigot membelah menjadi dua embrio sehingga materi genetiknya sangat mirip."
    },
    {
        "soal": "Hormon yang membantu merangsang kontraksi otot rahim selama proses persalinan adalah ...",
        "pilihan": [
            "Oksitosin",
            "Melatonin",
            "Tiroksin",
            "Kortisol"
        ],
        "jawaban": 0,
        "pembahasan": "Oksitosin berperan membantu merangsang kontraksi otot rahim selama persalinan."
    },
    {
        "soal": "Metode kontrasepsi KB yang juga dapat membantu mengurangi risiko penularan infeksi menular seksual (IMS) adalah ...",
        "pilihan": [
            "Kondom",
            "Pil KB",
            "Suntik KB",
            "Vasektomi"
        ],
        "jawaban": 0,
        "pembahasan": "Kondom merupakan metode penghalang yang menghalangi pertemuan sperma dan sel telur serta dapat membantu mengurangi risiko penularan IMS."
    },
    {
        "soal": "Gangguan pada sistem reproduksi perempuan ketika jaringan menyerupai lapisan endometrium tumbuh di luar rahim disebut ...",
        "pilihan": [
            "Varikokel",
            "Endometriosis",
            "Epididimitis",
            "Prostatitis"
        ],
        "jawaban": 1,
        "pembahasan": "Endometriosis terjadi ketika jaringan yang menyerupai lapisan endometrium tumbuh di luar rahim, sehingga dapat memicu nyeri panggul dan gangguan menstruasi."
    },
]


# ==================================================
# HALAMAN HOME
# ==================================================

def home(request):
    return render(request, "core/home.html")


# ==================================================
# HALAMAN DASHBOARD
# ==================================================

def dashboard(request):
    return render(request, "core/dashboard.html")


# ==================================================
# DAFTAR MATERI
# ==================================================

def daftar_materi(request):
    return render(request, "core/materi.html", {
        "daftar_materi": DAFTAR_MATERI
    })


# ==================================================
# DETAIL MATERI
# ==================================================

def detail_materi(request, slug):

    materi = next(
        (item for item in DAFTAR_MATERI if item["slug"] == slug),
        None
    )

    if materi is None:
        raise Http404("Materi tidak ditemukan")

    index = DAFTAR_MATERI.index(materi)

    sebelumnya = DAFTAR_MATERI[index - 1] if index > 0 else None

    selanjutnya = (
        DAFTAR_MATERI[index + 1]
        if index < len(DAFTAR_MATERI) - 1
        else None
    )

    return render(request, "core/detail_materi.html", {
        "materi": materi,
        "sebelumnya": sebelumnya,
        "selanjutnya": selanjutnya,
    })


# ==================================================
# VIDEO PEMBELAJARAN
# ==================================================

def video(request):
    return render(request, "core/video.html")


# ==================================================
# KUIS DAN EVALUASI
# ==================================================

def kuis(request):

    hasil = None
    jawaban_siswa = {}

    if request.method == "POST":

        benar = 0

        for nomor, soal in enumerate(SOAL_KUIS):

            pilihan = request.POST.get(f"soal_{nomor}")

            try:
                pilihan = int(pilihan)
            except (TypeError, ValueError):
                pilihan = -1

            jawaban_siswa[nomor] = pilihan

            if pilihan == soal["jawaban"]:
                benar += 1

        total = len(SOAL_KUIS)

        nilai = round((benar / total) * 100) if total else 0

        hasil = {
            "benar": benar,
            "total": total,
            "nilai": nilai,
        }

    soal_tampil = []

    for nomor, soal in enumerate(SOAL_KUIS):

        data = soal.copy()
        data["nomor"] = nomor
        data["jawaban_teks"] = soal["pilihan"][soal["jawaban"]]
        data["jawaban_siswa"] = jawaban_siswa.get(nomor)

        soal_tampil.append(data)

    return render(request, "core/kuis.html", {
        "soal_kuis": soal_tampil,
        "hasil": hasil,
    })