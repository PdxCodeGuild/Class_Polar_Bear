from django.shortcuts import render, reverse
from .models import Supplier, Manufacturer, Customer
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def manufacturing(request):
    '''context = {
        'message': 'Hello World!'
    }
    return render(request, 'valuechain/index.html', context)'''

    supplier_datas = Supplier.objects.all()
    manufacturer_datas = Manufacturer.objects.all()
    customer_datas = Customer.objects.all()
    context = {
        'supplier_datas': supplier_datas,
        'manufacturer_datas': manufacturer_datas,
        'customer_datas': customer_datas
    }

    return render(request, 'valuechain/index.html', context)

def save_supplier(request):
    # print(request.POST)
    # return HttpResponse('form received')
    supplierid = request.POST['supplierid']
    capacity = request.POST['capacity']
    quality = request.POST['quality']
    timeliness = request.POST['timeliness']
    capacity_ave = request.POST['capacity_ave']
    quality_ave = request.POST['quality_ave']
    timeliness_ave = request.POST['timeliness_ave']
    item_id = request.POST['item_id']
    item_value = request.POST['item_value']

    supplier = Supplier(supplierid=supplierid, capacity=capacity, quality=quality, timeliness=timeliness, capacity_ave=capacity_ave, quality_ave=quality_ave, timeliness_ave=timeliness_ave, item_id=item_id, item_value=item_value)
    supplier.save()
    return HttpResponseRedirect(reverse('valuechain:manufacturing'))

# JSON Save Supplier

def jsave_supplier(request):
    data = json.loads(request.body)
    supplier = Supplier()
    supplier.supplierid = data['supplierid']
    supplier.capacity = data['capacity']
    supplier.quality = data['quality']
    supplier.timeliness = data['timeliness']
    supplier.capacity_ave = data['capacity_ave']
    supplier.quality_ave = data['quality_ave']
    supplier.timeliness_ave = data['timeliness_ave']
    supplier.item_id = data['item_id']
    supplier.item_value = data['item_value']
    supplier.save()
    return JsonResponse({'status': 'ok'})

def save_manufacturer(request):
    # print(request.POST)
    # return HttpResponse('form received')
    manufacturer_id = request.POST['manufacturer_id']
    m_capacity = request.POST['m_capacity']
    m_quality = request.POST['m_quality']
    m_timeliness = request.POST['m_timeliness']
    m_capacity_ave = request.POST['m_capacity_ave']
    m_quality_ave = request.POST['m_quality_ave']
    m_timeliness_ave = request.POST['m_timeliness_ave']
    agg_sys_id = request.POST['agg_sys_id']
    agg_sys_value = request.POST['agg_sys_value']

    manufacturer = Manufacturer(manufacturer_id=manufacturer_id, m_capacity=m_capacity, m_quality=m_quality, m_timeliness=m_timeliness, m_capacity_ave=m_capacity_ave, m_quality_ave=m_quality_ave, m_timeliness_ave=m_timeliness_ave, agg_sys_id=agg_sys_id, agg_sys_value=agg_sys_value)
    manufacturer.save()
    return HttpResponseRedirect(reverse('valuechain:manufacturing'))

def save_customer(request):
    # print(request.POST)
    # return HttpResponse('form received')
    customer_id = request.POST['customer_id']
    c_capacity = request.POST['c_capacity']
    c_quality = request.POST['c_quality']
    c_timeliness = request.POST['c_timeliness']
    c_capacity_ave = request.POST['c_capacity_ave']
    c_quality_ave = request.POST['c_quality_ave']
    c_timeliness_ave = request.POST['c_timeliness_ave']
    c_sys_id = request.POST['c_sys_id']
    c_sys_value = request.POST['c_sys_value']
    split_shipments = request.POST['split_shipments']

    customer = Customer(customer_id=customer_id, c_capacity=c_capacity, c_quality=c_quality, c_timeliness=c_timeliness, c_capacity_ave=c_capacity_ave, c_quality_ave=c_quality_ave, c_timeliness_ave=c_timeliness_ave, c_sys_id=c_sys_id, c_sys_value=c_sys_value, split_shipments=split_shipments)
    customer.save()
    return HttpResponseRedirect(reverse('valuechain:manufacturing'))
    

# JSON for Supplier

def get_supplier(request):
    suppliers = Supplier.objects.all()
    data = []
    for supplier in suppliers:
        data.append({
            'supplierid': supplier.supplierid,
            'capacity': supplier.capacity,
            'quality': supplier.quality,
            'timeliness': supplier.timeliness,
            'capacity_ave': supplier.capacity_ave,
            'quality_ave': supplier.quality_ave,
            'timeliness_ave': supplier.timeliness_ave,
            'item_id': supplier.item_id,
            'item_value': supplier.item_value,
        })

    return JsonResponse({'suppliers': data})

