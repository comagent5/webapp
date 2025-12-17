from django.db import models
from django.db.models import CharField, DateField, DecimalField, FloatField

from datetime import datetime

# Create your models here.
class MedocCodes(models.Model):
    """
    Таблиця архівом заказів кодів доступу
    """
    diler = CharField(max_length=50, verbose_name='Ділєр')
    edrpo = CharField(max_length=12, verbose_name=r'ЄДРПОУ/РНОКПП')
    name = CharField(max_length=80, verbose_name='Найменування клієнта')
    date_cod = DateField(verbose_name='Дата: діє до')
    type_cod = CharField(max_length=16, verbose_name='Тип коду доступа')
    sum_cl = DecimalField(max_digits=14, decimal_places=2, verbose_name='Вартість (клієнт)')
    sum_diler = DecimalField(max_digits=14, decimal_places=2, verbose_name='Вартість (ділєр)')
    date_zakaz = DateField(verbose_name='Дата заказу')
    module = CharField(max_length=20, verbose_name='Назва модулю')
    sum_comp = DecimalField(max_digits=14, decimal_places=2, verbose_name='Сума компенсації')
    note = CharField(max_length=80, verbose_name='Примітки')

    class Meta:
        app_label = 'medoc_app'
        db_table = 'medoc_codes'
        verbose_name = 'М.Е.Док Архів заказів'
        verbose_name_plural = 'М.Е.Док Архів заказів'
        ordering = ['date_cod', 'edrpo']
        managed = False
        required_db_vendor = 'postgresql'

    def __str__(self):
        name = str(self.name).strip()
        date = datetime.strftime(self.date_cod, '%d.%m.%Y')
        type_cod = str(self.type_cod).strip()
        return f'{name} {date} {type_cod}'

"""
CREATE TABLE IF NOT EXISTS public.medoc_codes
(
    id integer NOT NULL DEFAULT nextval('medoc_codes_id_seq'::regclass),
    diler character varying(50) COLLATE pg_catalog."default" NOT NULL,
    edrpo character varying(12) COLLATE pg_catalog."default" NOT NULL,
    name character varying(80) COLLATE pg_catalog."default" NOT NULL,
    date_cod date NOT NULL,
    type_cod character varying(16) COLLATE pg_catalog."default" NOT NULL,
    sum_cl numeric(14,2) NOT NULL,
    sum_diler numeric(14,2) NOT NULL,
    date_zakaz date NOT NULL,
    module character varying(20) COLLATE pg_catalog."default" NOT NULL,
    sum_comp numeric(14,2) NOT NULL,
    note character varying(80) COLLATE pg_catalog."default",
    CONSTRAINT medoc_codes_pkey PRIMARY KEY (id)
)
"""