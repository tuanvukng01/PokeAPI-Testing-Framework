
# 🚀 Advanced API Testing Framework with Reporting and CI Integration

## 📋 Description
This project is a robust and extensible API testing framework written in Python using `pytest`. It:
- ✅ Validates multiple API endpoints (e.g., PokeAPI in this example).
- ⏱️ Checks response codes, performance benchmarks, and JSON schema validity.
- ⚙️ Supports parameterized testing for flexible input combinations.
- 📊 Generates detailed HTML test reports.
- 🤖 Integrates with GitHub Actions for CI/CD automation.

## 🌟 Features
- **Core API Testing**: Validate endpoint connectivity, measure performance, and ensure data schema integrity.
- **Parameterized Testing**: Dynamically test multiple endpoints and parameters without duplicating code.
- **Error Logging & Reporting**: Generate detailed logs and visually appealing HTML reports for debugging and analysis.
- **Configurable Test Suite**: Easily adjust base URL, endpoints, and testing thresholds via a YAML configuration file.
- **CI/CD Integration**: Run automated tests seamlessly on code pushes, pull requests, or on a scheduled basis.

---

## 🛠️ Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/tuanvukng01/PokeAPI-Testing-Framework.git
cd PokeAPI-Testing-Framework
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure the Framework
Edit the `config/config.yaml` file to set:
- Base API URL
- API endpoints
- Performance thresholds
- Schema validation details

Example `config.yaml`:
```yaml
base_url: "https://pokeapi.co/api/v2/"
endpoints:
  - "pokemon"
  - "ability"
  - "type"
performance_threshold: 1.0  
```

### 4. Run the Tests
Run all tests:
```bash
pytest tests/ --html=reports/test_report.html --self-contained-html
```

Run a specific test:
```bash
pytest tests/test_endpoints.py
```

### 5. View Test Reports
Open the generated HTML report in the `reports/` directory:
```bash
open reports/test_report.html
```

---

## 🤝 CI/CD Integration

### GitHub Actions Workflow
This project includes a pre-configured CI workflow (`.github/workflows/ci.yaml`) that:
- Installs dependencies.
- Runs tests on code pushes and pull requests.
- Generates test reports.

Steps:
1. Push your changes to a GitHub repository.
2. Check the GitHub Actions tab for automated test results.

---

## 📂 Project Structure
```
advanced_api_testing_framework/
├─ config/
│  ├─ config.yaml         
│  ├─ schema_pokemon.json  
├─ tests/
│  ├─ conftest.py         
│  ├─ test_data_validation.py  
│  ├─ test_endpoints.py        
│  ├─ test_performance.py     
├─ utils/
│  ├─ helpers.py           
│  ├─ logger.py           
│  ├─ schema_validator.py 
├─ reports/                
├─ .github/
│  └─ workflows/
│     └─ ci.yaml          
├─ requirements.txt      
└─ README.md             
```

---

## 🧪 Example Test Cases
### 1. Endpoint Connectivity
- Ensure endpoints return a `200 OK` status.

### 2. Performance Validation
- Verify response times are below the defined threshold.

### 3. Schema Validation
- Ensure JSON responses match the defined schema (`schema_pokemon.json`).

---

## 💡 Future Enhancements
- Add support for OAuth or token-based authentication.
- Include performance benchmarking for concurrent API calls.
- Support additional testing frameworks like `locust` for load testing.

---

## 🤖 Technologies Used
- **Programming Language**: Python
- **Libraries**: `pytest`, `requests`, `jsonschema`
- **Tools**: GitHub Actions, Docker (optional for CI)

---

[//]: # (## 🏆 Credits)

[//]: # (Developed by [Your Name]&#40;https://github.com/yourusername&#41;.)

---

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.
