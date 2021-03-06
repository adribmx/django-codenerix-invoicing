# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-29 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0008_auto_20180126_1711'),
        ('codenerix_invoicing', '0003_auto_20180129_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesLines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('removed', models.BooleanField(default=False, editable=False, verbose_name='Removed')),
                ('price_recommended', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Recomended price base')),
                ('quantity', models.FloatField(verbose_name='Quantity')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Subtotal')),
                ('discounts', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Discounts')),
                ('taxes', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Taxes')),
                ('equivalence_surcharges', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Equivalence surcharge')),
                ('total', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10, verbose_name='Total')),
                ('code', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Code')),
                ('description_basket', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('price_base_basket', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price base')),
                ('discount_basket', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Discount (%)')),
                ('tax_basket', models.FloatField(blank=True, default=0, null=True, verbose_name='Tax (%)')),
                ('equivalence_surcharge_basket', models.FloatField(blank=True, default=0, null=True, verbose_name='Equivalence surcharge (%)')),
                ('tax_label_basket', models.CharField(blank=True, max_length=250, null=True, verbose_name='Tax Name')),
                ('notes_basket', models.CharField(blank=True, max_length=256, null=True, verbose_name='Notes')),
                ('description_order', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('price_base_order', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price base')),
                ('discount_order', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Discount (%)')),
                ('tax_order', models.FloatField(blank=True, default=0, null=True, verbose_name='Tax (%)')),
                ('equivalence_surcharge_order', models.FloatField(blank=True, default=0, null=True, verbose_name='Equivalence surcharge (%)')),
                ('tax_label_order', models.CharField(blank=True, max_length=250, null=True, verbose_name='Tax Name')),
                ('notes_order', models.CharField(blank=True, max_length=256, null=True, verbose_name='Notes')),
                ('notes_albaran', models.CharField(blank=True, max_length=256, null=True, verbose_name='Notes')),
                ('description_ticket', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('price_base_ticket', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price base')),
                ('discount_ticket', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Discount (%)')),
                ('tax_ticket', models.FloatField(blank=True, default=0, null=True, verbose_name='Tax (%)')),
                ('equivalence_surcharge_ticket', models.FloatField(blank=True, default=0, null=True, verbose_name='Equivalence surcharge (%)')),
                ('tax_label_ticket', models.CharField(blank=True, max_length=250, null=True, verbose_name='Tax Name')),
                ('notes_ticket', models.CharField(blank=True, max_length=256, null=True, verbose_name='Notes')),
                ('notes_ticket_rectification', models.CharField(blank=True, max_length=256, null=True, verbose_name='Notes')),
                ('description_invoice', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('price_base_invoice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price base')),
                ('discount_invoice', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Discount (%)')),
                ('tax_invoice', models.FloatField(blank=True, default=0, null=True, verbose_name='Tax (%)')),
                ('equivalence_surcharge_invoice', models.FloatField(blank=True, default=0, null=True, verbose_name='Equivalence surcharge (%)')),
                ('tax_label_invoice', models.CharField(blank=True, max_length=250, null=True, verbose_name='Tax Name')),
                ('notes_invoice', models.CharField(blank=True, max_length=256, null=True, verbose_name='Notes')),
                ('notes_invoice_rectification', models.CharField(blank=True, max_length=256, null=True, verbose_name='Notes')),
                ('albaran', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales', to='codenerix_invoicing.SalesAlbaran', verbose_name='Albaran')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales', to='codenerix_invoicing.SalesBasket', verbose_name='Basket')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales', to='codenerix_invoicing.SalesInvoice', verbose_name='Invoice')),
                ('invoice_rectification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales', to='codenerix_invoicing.SalesInvoiceRectification', verbose_name='Invoice rectification')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales', to='codenerix_invoicing.SalesOrder', verbose_name='Sales order')),
                ('product_final', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales', to='codenerix_products.ProductFinal', verbose_name='Product')),
                ('product_unique', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales', to='codenerix_products.ProductUnique', verbose_name='Product Unique')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales', to='codenerix_invoicing.SalesTicket', verbose_name='Ticket')),
                ('ticket_rectification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines_sales', to='codenerix_invoicing.SalesTicketRectification', verbose_name='Ticket rectification')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
        ),
    ]
