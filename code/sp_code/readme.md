`
ipython 

%load_ext autoreload 
%autoreload 2
import sp_triangel_closing as tc

listings = tc.find_listings(tc.records, '9336316')
fellow_travelers = tc.find_travelers(tc.records, listings)
triange_counts = tc.count_triangles(tc.records, fellow_travelers)      
tc.recommend_listings(triange_counts, listings)

`
