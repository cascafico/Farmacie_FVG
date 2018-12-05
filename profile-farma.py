# pharmacies update 

# aggiunge tag source=MDS
add_source = False
source = 'MDS'

# do not add unique reference IDs to OSM?

# aggiunge tag ref:<dataset_id>=<id del MDS>
# True -> relying only on geometric matching every time
no_dataset_id = True
dataset_id = 'mds'

# Overpass query to use when searching OSM for data
#overpass_timeout = 120 default
overpass_timeout = 300
#query = [('amenity', 'fuel'),('waterway', 'fuel')] both conditions
#query = [('amenity', 'fuel')],[('waterway', 'fuel')]  or condition
#query = [('amenity', 'fuel'),('disused:amenity','fuel')]  namespace disused and abandoned are implicit
#query = [('amenity', 'fuel'),('ref:mise','.*')] 
query = [('amenity', 'pharmacy')] 

# parameter --osm will use indipendently generated queries, ie:
# http://overpass-turbo.eu/s/BZq
# http://overpass-turbo.eu/s/BZM (amenity=fuel and fuel:cng or fuel:lpg not "yes" 
# use wget -O manual-query.osm <http_addr obtained exporting compact query>

# attenzione, coord errate possono rendere enorme il bbox
# use openrefine for lat lon ranges
# vantaggio: fa richieste multiple ad overpass
bbox = True

# italia
#bbox = [35.28,6.62,47.1,18.79]

# tags to replace on matched OSM objects
# troppi unmatched dovuti a formato ref:vatin non corretto:
#master_tags = ('operator','name','ref:vatin','dispensing','addr:housenumber','addr:street')
master_tags = ('source','operator','start_date','name','ref:vatin')

delete_unmatched = False
#tag_unmatched = { 'fixme':'questa farmacia può essere cambiata: controllare' }


# max distance to search for a match in meters
max_distance = 80
