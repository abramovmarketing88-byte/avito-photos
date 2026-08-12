# Фото для **услуг** (универсальный режим)

Параллель товарному `kuhni/` + `wardrobes/`, но одна ветка **`{disk_root}/{niche_slug}/`**.

## Структура на Диске

```text
/{DISK_ROOT}/                    # из брифа, напр. /AUTOZA/Brand_photos
  uslugi/                        # или services/, {brand}-services/
    sets/
      set-01-{slug}/
        raw-01-hero.jpg
        02-angle.jpg
        03-detail.jpg
        04-fomo.jpg
      set-02-… … set-10-…
    heroes/
      {Id}.jpg
```

`DISK_ROOT` и `niche_slug` — из брифа, **ASCII only**.

## Кластеры сетов (пример мебель-услуги)

| Кластер | Смысл сетов | Hero-исходники |
|---------|-------------|----------------|
| kitchen | 4 сета | готовая кухня в интерьере |
| wardrobe | 3 сета | шкаф-купе / прихожая |
| general | 3 сета | офис, под ключ, производство |

Подбор сета по **title** строки (keywords), не только `% 10`.

## Источники кадров (3 пула)

1. **hypotheses** — AI / постановочные (мастер, клиент, 3D, договор)
2. **stock-interior** — готовый результат в интерьере
3. **stock-process** — цех, ЧПУ, монтаж (не на hero для услуг)

**Hero услуг:** готовый результат / доверие; **не** абстрактная текстура, **не** только станок на обложке (research: 0/N factory-on-hero в топе).

Пропускать: чистый инструмент без продукта, склад без мебели, коллаж.

## Алгоритм (режим C для services)

1. Собрать 10 сетов × 4 → resize 1920×1440, оверлеи по [overlay-hooks.md](overlay-hooks.md)
2. На строку Excel: hero = overlay(hook + USP + CTA) → `heroes/{Id}.jpg`
3. ImageUrls: hero | 02 | 03 | 04; `ImageNames` пусто
4. Активные AvitoId — **не менять** без явного запроса пользователя
5. Бэкап xlsx → `output/backups/…-before-photos.xlsx`

## Маппинг колонок Excel

**Не assume** col 8 = ImageUrls. Прочитать header row шаблона:

```python
# services example
COL_URLS = 5   # ImageUrls
COL_TITLE = 10
SHEET = "…"    # из шаблона категории
DATA_START = 5
```

## URL

```
https://cloud-api.yandex.net/v1/disk/resources/download?path=/{DISK_ROOT}/uslugi/heroes/{Id}.jpg
```

Разделитель в ячейке: ` | ` (пробел-пайп-пробел).

## Скрипт-эталон

В проекте клиента: `scripts/build_{niche}_photos_and_urls.py` — копировать логику из боевого пайплайна, не хардкодить бренд.

Валидатор скилла: `scripts/validate_image_urls.py --expect 4`.
