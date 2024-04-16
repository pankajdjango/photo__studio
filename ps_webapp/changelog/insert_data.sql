INSERT INTO general.account_type (account_type) VALUES ('Client'), ('Photographer');

INSERT INTO general.event_status (status) values ('Pending'),('Confirm'),('Rejected'),('Cancel')

insert into general.event_type (event_name)
values
 ('Model Photography'),
 ('Portrait Photography'),
 ('Wedding Program Photography'),
 ('Child Photography'),
 ('Mature age Photography'),
 ('Fitness Photography'),
 ('Birthday-Party')
;

insert into general.role_master (role_name) values ('Admin');
insert into general.user_roles (role_id,userid) values (1,5);
