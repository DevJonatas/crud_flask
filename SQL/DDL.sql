CREATE TABLE student(
    id integer not null auto_increment,
    ra integer not null,
    cpf varchar(11) not null,
    first_name varchar(30) not null,
    last_name varchar(30) not null,
    phone varchar(11) not null,
    date_create DATE,
    date_update DATE,

    constraint pk_student primary key(id),
    constraint uk_student_ra unique(ra),
    constraint uk_student_cpf unique(cpf)
);

COMMIT;

