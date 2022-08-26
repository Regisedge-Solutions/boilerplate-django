from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    description = models.TextField(max_length=200, null=True, blank=True)
    featured = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    tags = models.ManyToManyField(CustomerTags)

    def __str__(self):
        return f'{self.name} ({self.email})' or ''

    # Abhinav : properties can be created for small functions. decorators 
    @property
    def display_name(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name_plural = "2. Customers" 
        verbose_name = "Customer"
        unique_together = (
             ('field1', 'field2',)
        )
        index_together = (
        ('field1', 'field2',)
        )
        ordering = ('name',)


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

FEATURED = (
    (0,'No'),
    (1,'Everywhere'),
    (2,'Category-only'),
)
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True) 
    category = models.CharField(max_length=200, null=True, choices = CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField('Active',null=True) # Specifying string in the beginning names the field for visual purposes
    tags = models.ManyToManyField(Tag)
    featured = models.IntegerField(choices=FEATURED, default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Status',max_length=200, null=True, choices = STATUS)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    street_1 = models.CharField(max_length=255)
    street_2 = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=20)
    country = CountryField()
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} ({self.email})'


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, related_name='purchases')
    placed_at = models.DateTimeField(default=timezone.now)
    shipped_at = models.DateTimeField(blank=True, null=True)
    discount_code = models.CharField(blank=True, default='', max_length=20)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    shipped = models.BooleanField(default=False)
    items = models.ManyToManyField('products.Product', through='PurchaseItem')


class PurchaseItem(models.Model):
    product = models.ForeignKey('products.Product')
    purchase = models.ForeignKey(Purchase)
    quantity = models.IntegerField(default=1)


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    location = models.CharField(max_length=10, unique=True)
    serial_number = models.CharField(max_length=40, unique=True)
    quantity = models.IntegerField()
    categories = models.ManyToManyField('Category')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})


def _image_upload(instance, filename):
    return f'products/{instance.product.slug}/{filename}'


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images')
    order = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to=_image_upload)

    class Meta:
        ordering = ['order']
        unique_together = ('product', 'order')

    def __str__(self):
        return f'Image {self.order} for {self.product}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # Abhinav : properties can be created for small functions. decorators 
    @property
    def display_name(self):
        return f'{self.name} ({self.email})'



class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

FEATURED = (
    (0,'No'),
    (1,'Everywhere'),
    (2,'Category-only'),
)
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True) 
    category = models.CharField(max_length=200, null=True, choices = CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField('Active',null=True) # Specifying string in the beginning names the field for visual purposes
    tags = models.ManyToManyField(Tag)
    featured = models.IntegerField(choices=FEATURED, default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Status',max_length=200, null=True, choices = STATUS)




