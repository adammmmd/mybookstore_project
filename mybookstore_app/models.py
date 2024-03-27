from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class TabelBuku (models.Model):
    id_buku = models.CharField(max_length=7)
    kategori = models.CharField(max_length=20)
    nama_buku = models.CharField(max_length=200)
    penulis = models.CharField(max_length=200)
    deskripsi = models.TextField()
    halaman = models.IntegerField()
    harga = models.IntegerField()
    stok = models.IntegerField()
    penerbit = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images', blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.cover.url))
    image_tag.short_description = 'Cover'

class TabelPenerbit (models.Model):
    id_penerbit = models.CharField(max_length=7)
    logo = models.ImageField(upload_to='images', blank=True, null=True)
    nama = models.CharField(max_length=200)
    alamat = models.TextField()
    kota = models.CharField(max_length=100)
    telepon = models.CharField(max_length=20)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.logo.url))
    image_tag.short_description = 'Logo'