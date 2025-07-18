# Internship Report: AI-Powered Geo-Spatial Property Tax Intelligence and Flagging System

**Organization:** Airawat Research Foundation

**Team Members:**
* Amit Kumar
* Daxal Prajapati
* Karunaya Garg
* Navya Nihal

## Table of Contents
1.  [Problem Statement](#problem-statement)
2.  [Proposed AI Solution](#proposed-ai-solution)
    * [Idea Summary](#idea-summary)
    * [Key Features](#key-features)
    * [Product Overview](#product-overview)
    * [Flowchart](#flowchart)
3.  [Impact and Success Metrics](#impact-and-success-metrics)
4.  [Detailed Product Design & Workflow](#detailed-product-design--workflow)
    * [Modules](#modules)
    * [Model Pipeline](#model-pipeline)
    * [Deployment Design](#deployment-design)
5.  [Product Development Plan](#product-development-plan)
    * [Data Requirements (Pilot period)](#data-requirements-pilot-period)
    * [Data Pipeline](#data-pipeline)
    * [AI/ML Models](#aiml-models)
    * [Software Tools](#software-tools)
    * [Hardware Requirements](#hardware-requirements)
6.  [Execution & Integration Strategy](#execution--integration-strategy)
7.  [Potential Challenges and Risks](#potential-challenges-and-risks)
8.  [Future Scope](#future-scope)
9.  [References](#references)

---

## 1. Problem Statement

Urban Local Bodies (ULBs) in India frequently struggle with significant shortfalls in property tax collection. This issue stems from several factors, including unassessed constructions, chronic non-compliance, and weak data integration. Current tax recovery methods are largely manual, reactive, and localized, leading to inefficient governance.

### Domain/Industry Context:
ULBs face significant shortfalls in property tax collection due to unassessed constructions, chronic non-compliance, and weak data integration. Tax recovery remains highly manual, reactive, and localized, leading to inefficient governance.

### Traditional Methods:
Conventional systems rely on legacy surveys, manual record matching, and sporadic enforcement drives. There is limited use of real-time mapping or predictive flagging in day-to-day operations.

### Limitations of Existing Methods:
* Cannot detect newly constructed or unauthorized properties
* High human effort required for tracking non-compliance
* Poor integration between spatial and tax records
* No visual prioritization of enforcement zones

### Root Cause Analysis:
The primary root cause is the lack of a unified system that integrates geo-spatial property boundaries, usage types, and tax payment history. Existing datasets are underutilized and siloed, preventing early identification of defaulters.

## 2. Proposed AI Solution

### Idea Summary:
An AI-driven dashboard system that automatically flags property tax non-compliance using geo-spatial clustering and real-time visualization. The system will allow municipal staff to visualize, prioritize, and take action based on location-specific risk.

### Key Features:
* Automated clustering of properties by spatial and payment behavior
* Real-time flagging of non-compliant properties on map
* Visual zoning (Residential, Commercial, Industrial)

### Product Overview:
The tool will display property-level non-compliance and risk zones through an interactive map interface and generate auto-prioritized inspection lists. It uses unsupervised ML (e.g., HDBSCAN) and geospatial data fusion.

### Flowchart:

1.  **Ingest and Harmonize ULB Datasets:**
    Collect geo-tagged property records along with historical payment data and standardize across varying formats (e.g., Excel, GIS shapefiles, and SQL databases).

2.  **AI-Powered Clustering and Anomaly Detection:**
    Apply unsupervised algorithms (like HDBSCAN) to spatially cluster properties and identify statistically significant anomalies in payment behavior, construction patterns, or tax under-assessment.

    * **Clusters based on property type:**
        *(Image/Diagram of property type clusters would go here, if available)*

    * **Cluster with unpaid property tax:**
        *(Image/Diagram of unpaid property tax clusters would go here, if available)*

    * **Unpaid Property tax Clusters:**
        *(Image/Diagram of unpaid property tax clusters would go here, if available)*

3.  **Dynamic Geo-Spatial Visualization:**
    Generate interactive maps displaying high-risk zones, defaulter clusters, and unassessed property pockets, overlaid with zoning classifications (residential, commercial, etc.).

    * **Defaulter clusters:**
        *(Image/Diagram of defaulter clusters would go here, if available)*

    * **Defaulter’s heatmap:**
        *(Image/Diagram of defaulter's heatmap would go here, if available)*

4.  **Automated Prioritization and Decision Support:**
    Provide municipal officials with AI-generated inspection shortlists, risk-ranked properties, and zone-level policy recommendations to streamline enforcement and improve tax recovery.

## 3. Impact and Success Metrics

### Key Goals:
* Improve property tax compliance using data-driven methods
* Reduce manual inspection and coverage gaps
* Detect unauthorized or under-assessed properties

## 4. Detailed Product Design & Workflow

### Modules:
* Geo-clustering of properties
* Anomaly detection based on payment irregularity
* Zoning engine (based on land-use tagging)
* Interactive inspection dashboard
* Exportable inspection/notice lists

### Model Pipeline:
* **Input:** Geo-coordinates, payment history, property type
* **ML:** HDBSCAN clustering + rule-based anomaly logic
* **Output:** Flagged properties, cluster maps

### Deployment Design:
* Web-based dashboard
* Backend with FastAPI + Python models
* Database: PostgreSQL + PostGIS for spatial indexing

## 5. Product Development Plan

### Data Requirements (Pilot period):
* **Property ID (PID):** Unique identifier assigned to each property.
* **Tax collection data (multi-year):** Historical records of property tax assessments and payments over several years.
* **Property coordinates (lat/lon):** Geographical location of the property captured as latitude and longitude.
* **Property type/zoning metadata:** Classification of property based on use (residential, commercial, mixed use, industrial) and zoning regulations.
* **Optional: Construction permits or floor-area maps:** Official documentation of approved construction details, building permits, and mapped built-up areas for compliance and valuation.

### Data Pipeline:
* We will require data from the ULB that would be having a fixed format of columns so that the data might not require much cleaning and augmentation.
* We make different geo-spatial clusters on the map of the ULB with boundaries defined to the cluster, marking it as residential, commercial, etc.
* **Feature engineering:** payment delays, land usage, density

### AI/ML Models:
* **Clustering using HDBSCAN for flexible zoning:** Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN) is a powerful and versatile clustering algorithm. Unlike K-Means algorithm it doesn’t rely on the assumption that clusters are always spherical or elliptical. HDBSCAN can generate clusters that are arbitrary in shape, and need not be of certain pre-specified shape. This enhances the practical applicability of the algorithm for clustering zones in the ULB.
* **Anomaly detection:** We have integrated a system which when fed by data, can detect and flag anomalies like property tax not paid or if a property is built or modified without permissions from the required government bodies.
* **Tools:** Scikit-learn, Pandas, Numpy

### Software Tools:

| Category          | Technology / Framework | Description / Purpose                                      |
| :---------------- | :--------------------- | :--------------------------------------------------------- |
| Programming       | Python                 | Main programming language for backend and scripting        |
| Web Framework     | FastAPI                | High-speed Python framework for building APIs              |
| GIS Software      | QGIS                   | Desktop GIS for spatial analysis and visualization         |
| Database          | PostgreSQL             | Relational database for storing structured data            |
| Spatial Extender  | PostGIS                | Extension adding spatial (GIS) capabilities to Postgres    |

### Hardware Requirements:
* Cloud VM or ULB-hosted server
* No GPU needed; can run on standard hardware

## 6. Execution & Integration Strategy

* **Phase 1:** Pilot compliance analytics on 10,000 Indore ULB properties, standardizing data and testing detection models via dashboard.
* **Phase 2:** Integrate UPYOG tax APIs for automated, real-time tax data synchronization and workflow triggers.
* **Phase 3:** Link water and electricity billing to identify compliance gaps, generating unified risk alerts.
* **Field team training:** Train teams with dashboard walkthroughs and practical exercises to build on-ground effectiveness.
* **Validation:** Cross-check system results with past enforcement outcomes, refining models for accuracy.
* **Maintenance:** Retrain models monthly incorporating ULB feedback and enforcement data for continuous improvement.

## 7. Potential Challenges and Risks

* **Missing or inconsistent geo-coordinates in ULB datasets:** Inaccurate or absent location data hampers the ability to map and validate properties spatially, leading to gaps in assessment and enforcement.
* **Delay in data sharing from state departments:** Slow or restricted information flow between agencies stalls property updates, compliance tracking, and coordinated action.
* **Difficulty integrating legacy records with spatial databases:** Old paper or non-standard digital records often lack structured spatial references, complicating their migration to modern GIS-based systems.
* **Risk of over-flagging without human validation:** Automated systems may incorrectly flag compliant properties as anomalous or non-compliant if not cross-checked by knowledgeable staff.
* **Resistance from staff to AI recommendations:** Employees may distrust, misunderstand, or oppose decision-support outputs from AI-driven models, slowing adoption and reducing operational effectiveness.

## 8. Future Scope

* **Integration with Remote Sensing & Drone Imagery:** Leverage satellite data or drone surveillance to detect illegal constructions, unauthorized extensions, and land use violations that escape manual inspections.
* **Grievance System Integration:** Connect with Public Grievance Redressal (PGR) platforms to correlate complaints (e.g., encroachments, billing issues) with non-compliant or high-risk properties.
* **Revenue Forecasting Module:** Develop AI models to forecast future property tax revenue based on zone-wise trends, seasonal behavior, and historical compliance patterns—supporting ULB budgeting and planning.
* **Predictive Enforcement Recommendations:** Use machine learning to identify patterns in previous enforcement actions and generate proactive inspection targets, reducing dependency on reactive operations.
* **Citizen-Facing Transparency Tools:** Enable citizens to verify their property records, payment status, and zoning classification through interactive public portals—building trust and encouraging voluntary compliance.
* **Cross-Service Data Integration:** Integrate with other urban services such as water supply, electricity, and sanitation to build a 360° compliance profile for each property, enabling coordinated municipal action.

## 9. References

* UPYOG API, Architecture – MoHUA
* HDBSCAN Documentation – hdbscan.readthedocs.io
* QGIS – Open-source GIS Tool
* Prof. Nisheeth Srivastava – IIT Kanpur, Spatial Tax Insights
