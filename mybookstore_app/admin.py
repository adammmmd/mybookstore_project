from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.


admin.site.site_header = "Admin mybookstore"
admin.site.site_title = "mybookstore"
admin.site.index_title = "Admin mybookstore"

class TabelBukuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'id_buku', 'kategori', 'nama_buku', 'penulis', 'deskripsi', 'halaman', 'harga', 'stok', 'penerbit', 'image_tag')
    list_filter = ('id_buku', 'kategori', 'nama_buku', 'penulis', 'deskripsi', 'halaman', 'harga', 'stok', 'penerbit')
    search_fields = ('id_buku', 'kategori', 'nama_buku', 'penulis', 'deskripsi', 'halaman', 'harga', 'stok', 'penerbit')

admin.site.register(TabelBuku, TabelBukuAdmin)


class TabelPenerbitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'id_penerbit','image_tag', 'nama', 'alamat', 'kota', 'telepon')
    list_filter = ('id_penerbit','logo', 'nama', 'alamat', 'kota', 'telepon')
    search_fields = ('id_penerbit','logo', 'nama', 'alamat', 'kota', 'telepon')

admin.site.register(TabelPenerbit, TabelPenerbitAdmin)
