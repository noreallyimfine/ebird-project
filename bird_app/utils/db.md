# Database Schema

  ### States:
      state: varchar(15) primary key

  ### Counties:
      ID: incremnter. primary key
      state: varchar(15) foreign key
      county: varchar(30)
  
  ### Regions:
      state: varchar(15)
      county: varchar(30)
      region: varchar(15)

  ### Birds:
      name: varchar(30) primary key
    
  ### Lookup table?