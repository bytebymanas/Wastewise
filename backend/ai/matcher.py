# backend/ai/matcher.py
from ..models import Listing

def find_matches(listing_id):
    current_listing = Listing.query.get(listing_id)
    
    # Simple matching: same material type within 100km radius
    matches = Listing.query.filter(
        Listing.material_type == current_listing.material_type,
        Listing.id != listing_id
    ).all()
    
    return matches
