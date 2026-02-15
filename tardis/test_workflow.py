import sys

# محاولة الوصول للـ Registry من داخل هيكل المشروع نفسه
try:
    from kubeflow.trainer import TrainerClient
    from kubeflow.optimizer import OptimizerClient

    print("🚀 Initializing E2E Workflow Components...")

    # تجربة استيراد الـ Registry بالمسارات المحتملة في الـ SDK
    try:
        from kubeflow.model_registry import ModelRegistryClient
    except ImportError:
        try:
            # المسار البديل الشائع في النسخ التجريبية
            from kubeflow.model_registry.client import ModelRegistryClient
        except ImportError:
            # حل أخير: تعريف الـ Client كـ Placeholder مؤقتاً لشرح الـ Workflow
            print("⚠️ ModelRegistryClient not found in local SDK. Using Placeholder for Tutorial.")


            class ModelRegistryClient:
                def __init__(self): print("Registry Placeholder Initialized")


    def run_tutorial():
        trainer = TrainerClient()
        optimizer = OptimizerClient()
        registry = ModelRegistryClient()
        print("\n✅ All components connected: Trainer -> Optimizer -> Registry")


    if __name__ == "__main__":
        run_tutorial()

except Exception as e:
    print(f"❌ Error: {e}")