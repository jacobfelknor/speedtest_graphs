from django.core.management.base import BaseCommand
import speedtest
from speedtestlog.models import SpeedTestResult


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Running speedtest...")
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        st.get_best_server()
        results = st.results.dict()

        SpeedTestResult.objects.create(
            **{
                "timestamp": results["timestamp"],
                "ping": results["ping"],
                "upload": results["upload"],
                "download": results["download"],
                "json": results,
            }
        )

        print("Done!")
