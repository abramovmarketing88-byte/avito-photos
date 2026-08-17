# Фото для **услуг** (универсальный режим)

Параллель товарному `kuhni/` + `wardrobes/`, но одна ветка **`{disk_root}/{niche_slug}/`**.

## Структура на Диске

```text
/{DISK_ROOT}/                    # из брифа, напр. /AUTOZA/uslugi
  uslugi/                        # или services/, {brand}-services/
    {theme}/                     # опционально: marketplaces, construction, general
      sets/
        set-01-{slug}/
          01-hero.jpg            # или raw-01-hero.jpg
          02-angle.jpg
          03-detail.jpg
          04-fomo.jpg
          05-cta.jpg             # storyline
      heroes/
        {Id}.jpg
```

`DISK_ROOT` и `niche_slug` — из брифа, **ASCII only**.

## Живой эксперт (обязательно для консалтинга/бух/мед)

| ✅ Делать | ❌ Не делать |
|----------|-------------|
| Лицо эксперта/клиента на hero и слайдах | Однотонный фон + только текст (PIL) |
| Reference photos из брифа при AI-генерации | Stock с watermark / чужие лица |
| Офис, мягкий свет, «живое» фото | Абстрактные текстуры на обложке |
| PDF-референс с людьми → генерация с людьми | Вырезать людей «для простоты» |

**Hero услуг:** доверие + узнаваемый эксперт; **не** абстрактная текстура, **не** только станок/инструмент на обложке.

После генерации: **center-crop 4:3 → 1920×1440**.

## Режимы

| Режим | Когда | См. |
|-------|-------|-----|
| C | 10 сетов × 4, массовый фид | [sets-pipeline.md](sets-pipeline.md) |
| D | Storyline: N тем × 4–5 кадров | [storyline-sets.md](storyline-sets.md) |

Подбор сета/темы по **title** строки (keywords), не только `% 10`.

## Источники кадров (3 пула)

1. **hypotheses** — AI / постановочные (эксперт, клиент, договор) + **reference photos клиента**
2. **stock-interior** — готовый результат в интерьере
3. **stock-process** — процесс (не на hero для услуг)

Пропускать: чистый инструмент без человека/результата, коллаж, gradient-only.

## Алгоритм (режим C для services)

1. Собрать 10 сетов × 4 → люди где уместно → 1920×1440, оверлеи по [overlay-hooks.md](overlay-hooks.md)
2. На строку Excel: hero = overlay(hook + USP + CTA) → `heroes/{Id}.jpg`
3. ImageUrls: hero | 02 | 03 | 04; `ImageNames` пусто
4. Активные AvitoId — **не менять ImageUrls** без явного запроса
5. Бэкап xlsx → `output/backups/…-before-photos.xlsx`
6. Перегенерация: **заменить** старые cloud-api URL того же path, не дублировать

## Маппинг колонок Excel

**Не assume** col 8 = ImageUrls. Прочитать header row шаблона:

```python
# services example (зависит от шаблона!)
COL_URLS = 5   # ImageUrls — часто col 5 для услуг
COL_TITLE = 10
SHEET = "…"    # из шаблона категории
DATA_START = 4 # или 5 — проверить по шаблону
```

## URL

```
https://cloud-api.yandex.net/v1/disk/resources/download?path=/{DISK_ROOT}/uslugi/{theme}/heroes/{Id}.jpg
```

Разделитель в ячейке: ` | ` (пробел-пайп-пробел).

## Скрипт-эталон

В проекте клиента: `scripts/build_{niche}_photos_and_urls.py`, `prepare_storyline_assets.py`, `assign_storyline_photos.py`.

Валидатор: `scripts/validate_image_urls.py --expect 4`.

Pre-launch: [prelaunch-checklist.md](prelaunch-checklist.md).
