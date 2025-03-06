-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find crime scene description.
SELECT
    description
FROM
    crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28
    AND street = 'Humphrey Street';

-- Find out about bakery in the interviews.
SELECT
    transcript
FROM
    interviews
WHERE year = 2021 AND month = 07 AND day = 28
    AND transcript LIKE '%bakery%';

-- Find out the license plate of the thief
SELECT
    license_plate,
    year,
    month,
    day,
    minute,
    hour,
    activity
FROM
    bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28
    AND hour = 10 AND minute >= 15 AND minute <=25
    AND activity = 'exit';

-- Find any transactions before the theft.
SELECT
    account_number,
    amount
FROM
    atm_transactions
WHERE year = 2021 AND month = 7 AND day = 28
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw';

-- Find the data of the thief based on the atm transaction and bakery leaving.
SELECT
    thief.name,
    thief.phone_number,
    thief.passport_number,
    bakery.license_plate,
    atm.account_number
FROM
    people AS thief
JOIN bakery_security_logs AS bakery ON thief.license_plate = bakery.license_plate
JOIN bank_accounts AS bank ON thief.id = bank.person_id
JOIN atm_transactions AS atm ON bank.account_number = atm.account_number
WHERE atm.year = 2021 AND atm.month = 7 AND atm.day = 28
    AND atm.atm_location = 'Leggett Street'
    AND atm.transaction_type = 'withdraw'
    AND bakery.year = 2021 AND bakery.month = 7 AND bakery.day = 28
    AND bakery.hour = 10 AND bakery.minute >= 15 AND bakery.minute <= 25
    AND bakery.activity = 'exit';

-- Check found data in term of "minute or less" phone calls in the day of the crime.
SELECT
    thief.name,
    thief.passport_number,
    thief.license_plate,
    phone.caller,
    phone.receiver,
    phone.duration,
    bank.account_number
FROM people AS thief
JOIN phone_calls AS phone ON thief.phone_number = phone.caller
JOIN bank_accounts AS bank ON thief.id = bank.person_id
JOIN atm_transactions AS atm ON bank.account_number = atm.account_number
JOIN bakery_security_logs AS bakery ON thief.license_plate = bakery.license_plate
WHERE atm.year = 2021 AND atm.month = 7 AND atm.day = 28
    AND atm.atm_location = 'Leggett Street'
    AND atm.transaction_type = 'withdraw'
    AND bakery.year = 2021 AND bakery.month = 7 AND bakery.day = 28
    AND bakery.hour = 10 AND bakery.minute >= 15 AND bakery.minute <= 25
    AND bakery.activity = 'exit'
    AND phone.year = 2021 AND phone.month = 7 AND phone.day = 28
    AND phone.duration <= 60;

-- Find the earliest flight the day after the crime.
SELECT
    origin.abbreviation AS o_abbreviation,
    origin.full_name AS o_full_name,
    origin.city AS o_city,
    destination.abbreviation AS d_abbreviation,
    destination.full_name AS d_full_name,
    destination.city AS d_city,
    f1.hour,
    f1.minute
FROM airports AS origin
JOIN flights AS f1 ON origin.id = f1.origin_airport_id
JOIN airports AS destination ON destination.id = f1.destination_airport_id
WHERE f1.year = 2021 AND f1.month = 7 AND f1.day = 29
ORDER BY f1.hour, f1.minute
LIMIT 1;

-- Check if the suspect is among the passengers and which flight he chose.
SELECT
    thief.name,
    passengers.passport_number,
    passengers.seat,
    airports.full_name,
    airports.city
FROM people AS thief
JOIN passengers ON thief.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
JOIN airports ON flights.destination_airport_id = airports.id
JOIN phone_calls AS phone ON thief.phone_number = phone.caller
JOIN bank_accounts AS bank ON thief.id = bank.person_id
JOIN atm_transactions AS atm ON bank.account_number = atm.account_number
JOIN bakery_security_logs AS bakery ON thief.license_plate = bakery.license_plate
WHERE atm.year = 2021 AND atm.month = 7 AND atm.day = 28
    AND atm.atm_location = 'Leggett Street'
    AND atm.transaction_type = 'withdraw'
    AND bakery.year = 2021 AND bakery.month = 7 AND bakery.day = 28
    AND bakery.hour = 10 AND bakery.minute >= 15 AND bakery.minute <= 25
    AND bakery.activity = 'exit'
    AND phone.year = 2021 AND phone.month = 7 AND phone.day = 28
    AND phone.duration <= 60
    AND flights.year = 2021 AND flights.month = 7 AND flights.day = 29
    AND flights.hour = 8 AND flights.minute = 20;

-- Find an accomplice
SELECT
    accomplice.name
FROM
    people AS thief
JOIN passengers AS thief_passenger ON thief.passport_number = thief_passenger.passport_number
JOIN flights AS thief_flight ON thief_passenger.flight_id = thief_flight.id
JOIN phone_calls AS thief_call ON thief.phone_number = thief_call.caller
JOIN bank_accounts AS thief_account ON thief.id = thief_account.person_id
JOIN atm_transactions AS thief_transaction ON thief_account.account_number = thief_transaction.account_number
JOIN bakery_security_logs AS thief_log ON thief.license_plate = thief_log.license_plate
JOIN people AS accomplice ON thief_call.receiver = accomplice.phone_number
WHERE thief_flight.year = 2021 AND thief_flight.month = 7 AND thief_flight.day = 29
    AND thief_flight.hour = 8 AND thief_flight.minute = 20
    AND thief_transaction.year = 2021 AND thief_transaction.month = 7 AND thief_transaction.day = 28
    AND thief_transaction.atm_location = 'Leggett Street'
    AND thief_transaction.transaction_type = 'withdraw'
    AND thief_log.year = 2021 AND thief_log.month = 7 AND thief_log.day = 28
    AND thief_log.hour = 10 AND thief_log.minute >= 15 AND thief_log.minute <= 25
    AND thief_log.activity = 'exit'
    AND thief_call.year = 2021 AND thief_call.month = 7 AND thief_call.day = 28
    AND thief_call.duration <= 60;
