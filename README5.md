# Project Overview

This project is a **Smart Transport System** that includes an **authentication system** and a **Weight Classification & Loading Plan Generator**.

The program first verifies login credentials. After successful authentication, it accepts multiple weight inputs, validates them, classifies them into loading categories, and then applies a **Personalized Loading Impact (PLI)** rule based on the user’s name.

---

## Authentication System

The program allows access only when correct credentials are entered:

* **Username:** Aslam
* **Password:** SR310

If credentials are incorrect → access is denied.

---

## Personalization Details

* **Name used:** Aslam shaik
* **Length of name (without spaces) – L value:** 10
* **PLI Calculation:** `PLI = L % 3`
* **PLI Value:** 1

---

## Applied Personalization Rule

Since **PLI = 1**, the rule applied is:

➡️ **All items in the "Very Light" category are removed from the loading plan.**
These removed items are counted as **affected items due to PLI**.

---

## What the Program Produces

After login and weight entry, the system displays:

* Total valid weight entries
* Number of packages affected by PLI
* Final loading categories:

  * Very Light
  * Normal Load
  * Heavy Load
  * Overload
* Invalid weight entries
