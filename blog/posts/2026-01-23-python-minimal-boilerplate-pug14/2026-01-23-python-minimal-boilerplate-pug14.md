---
title: "Python Minimal Boilerplate: Presentation at PUG #14"
date: 2026-01-23
description: "Sharing the rationale behind the Python Minimal Boilerplate at the 14th Belgian Python User Group meetup in Mechelen."
tags: ["python", "boilerplate", "uv", "ruff", "meetup", "PUG"]
---

I recently had the opportunity to present at the 14th **Belgian Python User Group (PUG)** meetup. The event was kindly hosted by **Datashift** at their offices in Mechelen on January 22, 2026.

It was a fantastic evening of technical deep-dives and community networking. You can view the original meeting announcement and attendee list on [Meetup](https://www.meetup.com/python-user-group-belgium/events/312390657/).

<!-- more -->

## Meetup Agenda

The meetup featured three insightful sessions covering data engineering, project structure, and environment management:

* **Session 1: A modern data stack demo across engineering, quality, governance** *By [Arnaud Gueulette](https://www.linkedin.com/in/arnaud-gueulette/)* A hands-on demonstration of integrating leading DataOps and Data Governance tools to automate quality checks and orchestrate transformations.
* **Session 2: A modern template for Python projects (Python Minimal Boilerplate)** *By Lode Nachtergaele* I presented the rationale behind my template, which focuses on modern tools like `uv`, `ruff`, `ty`, `logfire`, and `zensical` to create a streamlined developer experience.
* **Session 3: From venv to isolated application directory: why virtualenvs are not enough** *By [Wouter Vanden Hove](https://www.linkedin.com/in/woutervh/)* A talk packed with tips and tricks from 20 years of experience on maintaining robust, isolated Python applications.

## Presentation Slides

Below are the slides from my talk. I discuss why a "minimal" boilerplate is essential for modern Python development and how it leverages the latest tools in the ecosystem.

<div class="responsive-iframe-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin-bottom: 2em;">
    <iframe
        src="https://docs.google.com/presentation/d/1JM3Yo0bXj0MsKEPuhYSUtPkbN3uaTX_SUwRZZMlSkuU/embed?start=false&loop=false&delayms=3000"
        frameborder="0"
        width="100%"
        height="569"
        allowfullscreen="true"
        mozallowfullscreen="true"
        webkitallowfullscreen="true"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
    </iframe>
</div>

## Check out the Project

The template is publicly available on GitHub. It is designed to be a "frictionless" starting point for any new Python project, ensuring you have the best tools configured from day one.

👉 **[cast42/python-minimal-boilerplate](https://github.com/cast42/python-minimal-boilerplate)**

Feel free to star the repo or open an issue if you have suggestions for further improvements!
