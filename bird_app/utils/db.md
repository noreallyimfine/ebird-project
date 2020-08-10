# Database Schema

  ### States:
      state: varchar(20) primary key

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
      region: varchar(20)
      season: varchar(10)
      bird: varchar(30)
      pct_of_total: float (DOUBLE?)