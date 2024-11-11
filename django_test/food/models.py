from django.db import models

class Item(models.Model):
    """
    Represents an item in the inventory system.
    
    This model stores information about individual items, including
    their name, description, price, and timestamps for creation and updates.
    """
    
    item_name = models.CharField(max_length=255, help_text="Name of the item")
    item_desc = models.TextField(help_text="Detailed description of the item")
    item_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Price of the item (up to 10 digits with 2 decimal places)"
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the item was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the item was last updated")

    def __str__(self):
        """
        String representation of the Item model.
        
        Returns:
            str: The name of the item.
        """
        return self.item_name

    class Meta:
        ordering = ['-created_at']  # Order items by creation date, newest first
        verbose_name = "Item"
        verbose_name_plural = "Items"