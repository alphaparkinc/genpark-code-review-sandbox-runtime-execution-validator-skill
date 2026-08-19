from client import CodeReviewSandboxRuntimeExecutionValidatorClient

def main():
    client = CodeReviewSandboxRuntimeExecutionValidatorClient()
    diff = "--- a/src/app.ts\n+++ b/src/app.ts\n@@ -10,1 +10,1 @@\n-  return data.total;\n+  return data?.total ?? 0;"
    res = client.validate_code_in_sandbox(diff)
    print(f"Validation Pass: {res['runtime_validation_pass']}")
    print(f"Review Score: {res['review_score']}/10")
    print(f"Exceptions Detected: {len(res['unhandled_exceptions_detected'])}")

if __name__ == "__main__":
    main()
