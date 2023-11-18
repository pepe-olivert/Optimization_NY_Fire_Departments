# Optimization_NY_Fire_Departments
You have recently been hired as analysts for the analytics department of the Fire Department of the City of New York. This department is in charge of managing, both at an strategic and operational level, everything related to the fire emergencies of the city. Therefore, it is one of the city's emergency departments and it plays a very important role in the welfare of the city.

The department is the largest in the United States, and it is also the second largest in the world. Therefore, the complexity of the department's organization is high, and so is the amount of resources to be managed. On the other hand, the tasks performed by this department are varied. Although the most obvious task is fire extinguishing, the city's fire department is also involved in the disposal of chemical and harmful materials, rescue operations, and medical emergencies in the city.

Currently, the fire department serves the five major boroughs that make up New York City:
* Manhattan: the nerve center of New York City, where most of the economic activity takes place and where the most luxurious housing is located.
* Brooklyn: The largest borough in population. In recent years it has become home to many families and young professionals due to the more reasonable prices compared to Manhattan and its vibrant artistic, creative and restaurant atmosphere.
* Bronx: One of the most culturally diverse boroughs in the city, with some of the most affordable housing. In the past it has been considered a problematic borough, but the quality of life has been gradually improving. However, it has not yet reached, on a general level, the safety standards of the other boroughs.
* Queens: This is the largest borough in terms of size. It is also less expensive than Manhattan and is it very well connected to it. However, travel times are longer as it is farther away than Brooklyn.
* Staten Island: This borough is sometimes forgotten because it is far from the rest. However, it also belongs to the city of New York. It is also the least populated of all the large boroughs. It concentrates less economic activity than the other boroughs.

At the operational level, the department is organized into companies. A company operates a single type of vehicle and it is specialized in the management of that vehicle and the tools carried on it. For the context of this project, there are 5 types of vehicles and, therefore, 5 types of companies to consider:

* Engine companies: They are in charge of extinguishing fires by means of the vehicle's water tank and the water available through the hydrants on the streets of New York. It has basic medical equipment, ground ladders and some basic tools. There are currently 197 vehicles of this type

* Ladder companies: They are in charge of forced entry, searching for people, ventilation, and tasks that require extensible ladders. There are currently 143 vehicles of this type.

* Rescue companies: These companies are highly specialized in special rescues that are beyond the scope of normal companies. They have vehicles equipped for rope rescues, building collapse rescues, confined space rescues, underground rescues, water rescues, and other scenarios. There are a total of 5 of these vehicles.

* Squad companies: These are hybrid companies that have the attributes of *ladder* and *engine* companies, but also have some tools for rescue and treatment of harmful substances. There are a total of 8 companies.

* Hazmat companies: These are companies specialized in the treatment of waste and materials harmful to life or the environment. There is only one company of this type.

These companies can be located in one of the 218 infrastructures that can serve as parking for firefighters and their vehicles. These infrastructures, which we will call as *stations*, are distributed throughout the city. The following map shows the distribution of these stations as well as some associated information.

The fire department primarily runs two shifts. The first shift, also known as the night shift, runs from 6 PM until 9 AM. The second shift runs from 9 AM to 6 PM.

The way the shifts work is as follows:
* Shifts start from one of 218 possible stations.
* The vehicle is parked at the assigned station until a new emergency to be covered arises.
* In the case of a new emergency, the firefighters leave with their vehicle to cover the assigned emergency.
* At the end of the emergency, they return to the station where the shift started.
* This process is repeated until the shift ends. In this case, the vehicle can stay at the station of the previous shift or be taken by the staff to a new station.

The city department wishes to optimize the location of these vehicles, as well as the assignment of service to New York neighborhoods.


## Some context considerations

Emergency services, as is the case of the fire department, are departments that seek both to serve as many people as possible and to do so in the shortest possible time. The former is due to the fact that it is a service for all citizens, so leaving any area uncovered would have significant negative effects on the image of the service. The second is due to the fact that in the case of emergencies, it is advisable to act as quickly as possible to minimize the damage to both the city's infrastructures and human lives.

New York City is comprised of its five major boroughs. Within the city's fire department, there are representatives and chief operating officers for each of the boroughs. They seek to respond to the needs of their stakeholders. The reality is that each of these boroughs is an influence group within the local and operational decisions of the department. Strongly favoring any one of the boroughs in service planning would mean major tensions and internal and external complaints.

In addition, for scarce resources such as squad or rescue companies, it is better not to group them in the same location, since it is interesting that they cover a wide geographic area. If a single borough concentrates all vehicles of the same type, it would again cause tensions within the department and at the city council level. Therefore, it has been suggested that the planning should consider the multi-district nature of New York City. The only exception is the hazmat vehicle, since only one of these resources is available.

In the eyes of the local administrators, it would also seem strange that when a station accommodates more than one vehicle, it contains all vehicles of the same type. This gives a sense of misallocation of available resources since those extra vehicles could be used to increase the area covered by the department.

Also, we should keep in mind that there are different types of emergencies covered by the fire department. That is, any vehicle cannot be used for everything. The frequency of these emergencies can be affected by different factors, both temporal and structural.

At shift change, ambulances should not travel long distances, as this causes a sense of increased work and fatigue for the workers making the trip between stations.

## Problem modelization

### Parameters of the model

* $β_ijk$: Represents the estimated demand in shift i of vehicles of type j in the neighbourhood k. It is computed as: $\[frac{N_ijk}{ \sum_{k=1}^{\K} N_ijk} * M_j \]$