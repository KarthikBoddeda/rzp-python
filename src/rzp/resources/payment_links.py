# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import payment_link_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payment_link import PaymentLink

__all__ = ["PaymentLinksResource", "AsyncPaymentLinksResource"]


class PaymentLinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/KarthikBoddeda/rzp-python#accessing-raw-response-data-eg-headers
        """
        return PaymentLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/KarthikBoddeda/rzp-python#with_streaming_response
        """
        return PaymentLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        currency: str,
        description: str,
        accept_partial: bool | NotGiven = NOT_GIVEN,
        callback_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        customer: payment_link_create_params.Customer | NotGiven = NOT_GIVEN,
        expire_by: int | NotGiven = NOT_GIVEN,
        first_min_partial_amount: int | NotGiven = NOT_GIVEN,
        notes: Dict[str, str] | NotGiven = NOT_GIVEN,
        notify: payment_link_create_params.Notify | NotGiven = NOT_GIVEN,
        reference_id: str | NotGiven = NOT_GIVEN,
        reminder_enable: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentLink:
        """
        Create a new payment link.
        [Docs](https://razorpay.com/docs/api/payments/payment-links/create-standard/)

        Args:
          amount: Amount in the smallest currency unit (e.g., paise)

          currency: ISO currency code

          description: Description of the payment link

          accept_partial: Allow partial payments

          callback_method: HTTP method for callback

          callback_url: Redirect URL after payment

          expire_by: Unix timestamp when the link expires

          first_min_partial_amount: Minimum amount for the first partial payment

          reference_id: Unique reference for the payment link

          reminder_enable: Enable reminders for the payment link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payment_links",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "description": description,
                    "accept_partial": accept_partial,
                    "callback_method": callback_method,
                    "callback_url": callback_url,
                    "customer": customer,
                    "expire_by": expire_by,
                    "first_min_partial_amount": first_min_partial_amount,
                    "notes": notes,
                    "notify": notify,
                    "reference_id": reference_id,
                    "reminder_enable": reminder_enable,
                },
                payment_link_create_params.PaymentLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentLink,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentLink:
        """
        Fetch a payment link by its unique ID.
        [Docs](https://razorpay.com/docs/api/payments/payment-links/fetch-id-standard/)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/payment_links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentLink,
        )


class AsyncPaymentLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/KarthikBoddeda/rzp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/KarthikBoddeda/rzp-python#with_streaming_response
        """
        return AsyncPaymentLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        currency: str,
        description: str,
        accept_partial: bool | NotGiven = NOT_GIVEN,
        callback_method: Literal["get", "post"] | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        customer: payment_link_create_params.Customer | NotGiven = NOT_GIVEN,
        expire_by: int | NotGiven = NOT_GIVEN,
        first_min_partial_amount: int | NotGiven = NOT_GIVEN,
        notes: Dict[str, str] | NotGiven = NOT_GIVEN,
        notify: payment_link_create_params.Notify | NotGiven = NOT_GIVEN,
        reference_id: str | NotGiven = NOT_GIVEN,
        reminder_enable: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentLink:
        """
        Create a new payment link.
        [Docs](https://razorpay.com/docs/api/payments/payment-links/create-standard/)

        Args:
          amount: Amount in the smallest currency unit (e.g., paise)

          currency: ISO currency code

          description: Description of the payment link

          accept_partial: Allow partial payments

          callback_method: HTTP method for callback

          callback_url: Redirect URL after payment

          expire_by: Unix timestamp when the link expires

          first_min_partial_amount: Minimum amount for the first partial payment

          reference_id: Unique reference for the payment link

          reminder_enable: Enable reminders for the payment link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payment_links",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "description": description,
                    "accept_partial": accept_partial,
                    "callback_method": callback_method,
                    "callback_url": callback_url,
                    "customer": customer,
                    "expire_by": expire_by,
                    "first_min_partial_amount": first_min_partial_amount,
                    "notes": notes,
                    "notify": notify,
                    "reference_id": reference_id,
                    "reminder_enable": reminder_enable,
                },
                payment_link_create_params.PaymentLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentLink,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentLink:
        """
        Fetch a payment link by its unique ID.
        [Docs](https://razorpay.com/docs/api/payments/payment-links/fetch-id-standard/)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/payment_links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentLink,
        )


class PaymentLinksResourceWithRawResponse:
    def __init__(self, payment_links: PaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = to_raw_response_wrapper(
            payment_links.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payment_links.retrieve,
        )


class AsyncPaymentLinksResourceWithRawResponse:
    def __init__(self, payment_links: AsyncPaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = async_to_raw_response_wrapper(
            payment_links.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payment_links.retrieve,
        )


class PaymentLinksResourceWithStreamingResponse:
    def __init__(self, payment_links: PaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = to_streamed_response_wrapper(
            payment_links.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payment_links.retrieve,
        )


class AsyncPaymentLinksResourceWithStreamingResponse:
    def __init__(self, payment_links: AsyncPaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = async_to_streamed_response_wrapper(
            payment_links.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payment_links.retrieve,
        )
