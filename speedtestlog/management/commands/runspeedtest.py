from django.core.management.base import BaseCommand
import speedtest
from speedtestlog.models import SpeedTestResult


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Running speedtest...")
        # speedtest results are MUCH lower on first run for some reason
        # run a "warm up" run, then use the results from the second run
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        st.get_best_server()
        # Run the second, more accurate run
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
