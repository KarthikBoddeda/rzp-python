# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rzp import Rzp, AsyncRzp
from rzp.types import PaymentLink
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Rzp) -> None:
        payment_link = client.payment_links.create(
            amount=1000,
            currency="INR",
            description="Payment for policy no",
        )
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Rzp) -> None:
        payment_link = client.payment_links.create(
            amount=1000,
            currency="INR",
            description="Payment for policy no",
            accept_partial=True,
            callback_method="get",
            callback_url="https://example-callback-url.com/",
            customer={
                "contact": "+919000090000",
                "email": "gaurav.kumar@example.com",
                "name": "Gaurav Kumar",
            },
            expire_by=1691097057,
            first_min_partial_amount=100,
            notes={"policy_name": "Jeevan Bima"},
            notify={
                "email": True,
                "sms": True,
            },
            reference_id="TS1989",
            reminder_enable=True,
        )
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Rzp) -> None:
        response = client.payment_links.with_raw_response.create(
            amount=1000,
            currency="INR",
            description="Payment for policy no",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = response.parse()
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Rzp) -> None:
        with client.payment_links.with_streaming_response.create(
            amount=1000,
            currency="INR",
            description="Payment for policy no",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = response.parse()
            assert_matches_type(PaymentLink, payment_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Rzp) -> None:
        payment_link = client.payment_links.retrieve(
            "id",
        )
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Rzp) -> None:
        response = client.payment_links.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = response.parse()
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Rzp) -> None:
        with client.payment_links.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = response.parse()
            assert_matches_type(PaymentLink, payment_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Rzp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payment_links.with_raw_response.retrieve(
                "",
            )


class TestAsyncPaymentLinks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncRzp) -> None:
        payment_link = await async_client.payment_links.create(
            amount=1000,
            currency="INR",
            description="Payment for policy no",
        )
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRzp) -> None:
        payment_link = await async_client.payment_links.create(
            amount=1000,
            currency="INR",
            description="Payment for policy no",
            accept_partial=True,
            callback_method="get",
            callback_url="https://example-callback-url.com/",
            customer={
                "contact": "+919000090000",
                "email": "gaurav.kumar@example.com",
                "name": "Gaurav Kumar",
            },
            expire_by=1691097057,
            first_min_partial_amount=100,
            notes={"policy_name": "Jeevan Bima"},
            notify={
                "email": True,
                "sms": True,
            },
            reference_id="TS1989",
            reminder_enable=True,
        )
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRzp) -> None:
        response = await async_client.payment_links.with_raw_response.create(
            amount=1000,
            currency="INR",
            description="Payment for policy no",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = await response.parse()
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRzp) -> None:
        async with async_client.payment_links.with_streaming_response.create(
            amount=1000,
            currency="INR",
            description="Payment for policy no",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = await response.parse()
            assert_matches_type(PaymentLink, payment_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRzp) -> None:
        payment_link = await async_client.payment_links.retrieve(
            "id",
        )
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRzp) -> None:
        response = await async_client.payment_links.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = await response.parse()
        assert_matches_type(PaymentLink, payment_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRzp) -> None:
        async with async_client.payment_links.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = await response.parse()
            assert_matches_type(PaymentLink, payment_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRzp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payment_links.with_raw_response.retrieve(
                "",
            )
