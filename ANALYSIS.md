# ANALYSIS

## Batch vs. Streaming Divergence

In this project, Apache Flink processes user interaction events continuously as they arrive from Apache Kafka. Unlike a batch processing system, which computes results after collecting all events, the streaming pipeline updates feature values in near real-time.

The implemented user features include:

* click_rate
* avg_dwell_time

The implemented content feature includes:

* engagement_rate

Batch processing waits until the entire dataset is available before calculating these values. Therefore, the feature values remain static until the next batch execution.

Streaming processing continuously updates feature values whenever new events arrive. As additional events are processed, the computed feature values change over time. This provides much fresher information for downstream machine learning models.

Small differences between batch and streaming results may occur because:

* Event-time window boundaries differ.
* Late events may arrive after some events have already been processed.
* Streaming windows continuously evolve while batch processing evaluates a fixed dataset.

Overall, streaming provides significantly lower latency and more up-to-date features compared to traditional batch processing.

---

## Late Event Handling

The pipeline uses Apache Flink Event-Time processing together with a Watermark Strategy.

A bounded out-of-orderness watermark of **30 seconds** was configured.

The producer intentionally generates a small percentage of late events to simulate real-world network delays.

The watermark allows events arriving within the configured tolerance to be processed correctly inside their event-time windows.

Events arriving after the watermark has advanced beyond the allowed threshold are considered excessively late and are not included in completed window computations.

This approach improves the correctness of feature computation while preventing windows from remaining open indefinitely.

The Flink pipeline successfully demonstrated:

* Event-Time processing
* 30-second Watermark handling
* 1-Hour Tumbling Window
* 15-Minute Sliding Window
* Real-time feature computation using Apache Kafka and Apache Flink
