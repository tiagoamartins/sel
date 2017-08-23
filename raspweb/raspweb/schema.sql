drop table if exists features;
create table features (
	heading text not null,
	subheading text,
	message text not null,
	image_path text
);
drop table if exists news;
create table news (
	heading text not null,
	subheading text,
	btn_text text,
	btn_link text,
	image_path text
);
drop table if exists members;
create table members (
	name text not null,
	job text,
	description text,
	photo text
);
