=======
Welcome
=======


Chetaa is a software-as-a-service (SaaS) platform designed to seamlessly connect 
logistics service providers with small business owners and customers who require 
fast, reliable, and efficient delivery solutions. The platform serves as an all-in-one ecosystem 
for managing logistics operations, optimizing delivery workflows, and ensuring timely fulfillment of customer requests.

Purpose
^^^^^^^

This documentation provides a structured guide to understanding and using Chetaa effectively. 
It is designed to cater to different user categories, including:

- Regular users - Individuals or businesses utilizing Chetaa for shipping and receiving packages.
- Logistics service providers – Businesses that manage deliveries, dispatch riders, and fleet operations.
- Administrators – System-level users who oversee platform operations, user management, and configurations.
- Developers – Internal and external engineers integrating Chetaa’s API into custom solutions or expanding its capabilities.

Contents
^^^^^^^^

The Chetaa documentation is a **comprehensive resource** that covers:

1. **How-To Guides**:  
   Step-by-step instructions for users navigating the platform, including setting up accounts, booking deliveries, and tracking shipments.

2. **Database Reference**:  
   A technical breakdown of Chetaa’s data structure, including key entities, relationships, and best practices for interacting with the database.

3. **API Documentation**:  
   A detailed reference for developers integrating Chetaa’s logistics API, including authentication, 
   endpoints, request-response formats, and sample use cases.

4. **User Role-Specific Guides**:  
   Tailored instructions for different user categories, ensuring each segment can maximize the platform’s potential.

Audience
^^^^^^^^

This documentation is intended for:

- **Regular users** looking for guidance on using Chetaa for their delivery needs.
- **Business owners** managing logistics for their products and services.
- **Logistics service providers** optimizing their operations.
- **Developers** working on integrating or extending Chetaa’s capabilities.

Whether you are a **business owner** looking for reliable logistics services or a **developer** seeking to integrate Chetaa into your application,
this guide provides all the necessary information to use, manage, and extend Chetaa efficiently.



.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :hidden:

   content/getting-started/overview
   content/getting-started/system-requirements
   content/getting-started/signup-login
   content/getting-started/dashboard
   content/getting-started/user-roles

.. toctree::
   :maxdepth: 2
   :caption: User Guide
   :hidden:

   content/user-guide/customers/index
   content/user-guide/business-owners/index
   content/user-guide/delivery/index
   content/user-guide/dispatchers/index


.. toctree::
   :maxdepth: 2
   :caption: Admin Guide
   :hidden:

   content/admin-guide/users
   content/admin-guide/config
   content/admin-guide/orders-payments
   content/admin-guide/performance

.. toctree::
   :maxdepth: 2
   :caption: Database Schema
   :hidden:

   content/database/
   content/database/tables/users
   content/database/tables/clients
   content/database/tables/customers
   content/database/tables/agents
   content/database/tables/delivery
   content/database/tables/app_delivery
   content/database/tables/delivery_logs
   content/database/tables/directory
   content/database/tables/dispatch
   content/database/tables/issue
   content/database/tables/issue_logs
   content/database/tables/notification
   content/database/tables/places
   content/database/tables/payments
   content/database/tables/transactions
   content/database/tables/services
   content/database/tables/subscription
   content/database/tables/wallet
   content/database/tables/withdrawals

.. toctree::
   :maxdepth: 2
   :caption: API Documentation
   :hidden:

   content/api-docs/overview
   content/api-docs/auth
   content/api-docs/endpoints/index
   content/api-docs/webhooks
   content/api-docs/errors

.. toctree::
   :maxdepth: 2
   :caption: Deployment & Configuration
   :hidden:

   content/deployment/install
   content/deployment/env-vars
   content/deployment/database
   content/deployment/hosting

.. toctree::
   :maxdepth: 2
   :caption: Security & Compliance
   :hidden:

   content/security/privacy
   content/security/payments
   content/security/auth
   content/security/fraud

.. toctree::
   :maxdepth: 2
   :caption: Troubleshooting & FAQs
   :hidden:

   content/troubleshooting/issues
   content/troubleshooting/support
   content/troubleshooting/bugs

.. toctree::
   :maxdepth: 2
   :caption: Contribution Guide
   :hidden:

   content/contribute/mkdocs
   content/contribute/contributing
   content/contribute/versioning

.. toctree::
   :maxdepth: 2
   :caption: Glossary & References
   :hidden:

   content/glossary/terms
   content/glossary/references

