# Case Data Wrangling : DVD Rental
This repo for learning purpose only

## 1. Preparation
Sebelum mencoba kode pada repository ini, pastikan anda sudah :
- **Install docker**. 
    - Ubuntu : https://docs.docker.com/engine/install/ubuntu/
    - Windows : https://docs.docker.com/desktop/install/windows-install/
    - Mac OS : https://docs.docker.com/desktop/install/mac-install/
- **Menyiapkan data source 3 yaitu database "dvdrental"**. 
    - Masuk ke direktori `preparation/data_source_3`
    - Jalankan perintah :
        ```
        docker compose up -d
        ```
- **Menyiapkan data warehouse (dvdrental_clean & dvdrental_analysis database).**
    - Masuk ke direktori `preparation/data_warehouse`
    - Jalankan perintah :
        ```
        docker compose up -d
        ```
    - Pada database dvdrental_clean, jalankan script berikut :
        ```sql
        -- Membuat skema public jika belum ada
        CREATE SCHEMA IF NOT EXISTS public;

        -- Buat tabel
        CREATE TABLE public.actor (
            actor_id SERIAL PRIMARY KEY,
            last_update TIMESTAMP,
            first_name VARCHAR,
            last_name VARCHAR
        );

        CREATE TABLE public.store (
            store_id SERIAL PRIMARY KEY,
            manager_staff_id INTEGER,
            address_id INTEGER,
            last_update TIMESTAMP
        );

        CREATE TABLE public.address (
            last_update TIMESTAMP,
            city_id INTEGER,
            address_id SERIAL PRIMARY KEY,
            district VARCHAR,
            phone VARCHAR,
            postal_code VARCHAR,
            address VARCHAR,
            address2 VARCHAR
        );

        CREATE TABLE public.category (
            category_id SERIAL PRIMARY KEY,
            last_update TIMESTAMP,
            name VARCHAR
        );

        CREATE TABLE public.city (
            city_id SERIAL PRIMARY KEY,
            country_id INTEGER,
            last_update TIMESTAMP,
            city VARCHAR
        );

        CREATE TABLE public.country (
            country_id SERIAL PRIMARY KEY,
            last_update TIMESTAMP,
            country VARCHAR
        );

        CREATE TABLE public.customer (
            active INTEGER,
            store_id INTEGER,
            create_date TIMESTAMP,
            last_update TIMESTAMP,
            customer_id SERIAL PRIMARY KEY,
            address_id INTEGER,
            activebool BOOLEAN,
            first_name VARCHAR,
            last_name VARCHAR,
            email VARCHAR
        );

        CREATE TABLE public.film_actor (
            actor_id SERIAL PRIMARY KEY,
            film_id INTEGER,
            last_update TIMESTAMP
        );

        CREATE TABLE public.film_category (
            film_id SERIAL PRIMARY KEY,
            category_id INTEGER,
            last_update TIMESTAMP
        );

        CREATE TABLE public.inventory (
            inventory_id SERIAL PRIMARY KEY,
            film_id INTEGER,
            store_id INTEGER,
            last_update TIMESTAMP
        );

        CREATE TABLE public.language (
            language_id SERIAL PRIMARY KEY,
            last_update TIMESTAMP,
            name VARCHAR
        );

        CREATE TABLE public.rental (
            rental_id SERIAL PRIMARY KEY,
            rental_date TIMESTAMP,
            inventory_id INTEGER,
            customer_id INTEGER,
            return_date TIMESTAMP,
            staff_id INTEGER,
            last_update TIMESTAMP
        );

        CREATE TABLE public.staff (
            picture VARCHAR,
            address_id INTEGER,
            store_id INTEGER,
            active BOOLEAN,
            last_update TIMESTAMP,
            staff_id SERIAL PRIMARY KEY,
            first_name VARCHAR,
            last_name VARCHAR,
            password VARCHAR,
            email VARCHAR,
            username VARCHAR
        );

        CREATE TABLE public.payment (
            payment_id SERIAL PRIMARY KEY,
            customer_id INTEGER,
            staff_id INTEGER,
            rental_id INTEGER,
            amount FLOAT,
            payment_date TIMESTAMP
        );

        CREATE TABLE public.film (
            fulltext VARCHAR,
            rating VARCHAR,
            last_update TIMESTAMP,
            film_id SERIAL PRIMARY KEY,
            release_year INTEGER,
            language_id INTEGER,
            rental_duration INTEGER,
            rental_rate FLOAT,
            length INTEGER,
            replacement_cost FLOAT,
            title VARCHAR,
            description VARCHAR,
            special_features VARCHAR
        );
        ```
    - Pada database dvdrental_analysis, jalankan script berikut :
        ```sql
        -- Membuat skema public jika belum ada
        CREATE SCHEMA IF NOT EXISTS public;

        -- Membuat tabel film_list
        CREATE TABLE public.film_list (
            fid SERIAL PRIMARY KEY,
            title VARCHAR,
            description VARCHAR,
            category VARCHAR,
            price FLOAT,
            length INTEGER,
            rating VARCHAR,
            actors VARCHAR
        );
        ```
- *Intall dependencies libraries**
    ```
    pip install -r requirements.txt
    ```

## 2. Usage
- Untuk melakukan validasi, gunakan perintah :
    ```
    python3 utils/data_validations.py
    ```
- Untuk melakukan exstrak -> transform -> load, gunakan perintah :
    ```
    python3 main.py
    ```